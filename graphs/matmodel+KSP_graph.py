import numpy as np
import matplotlib.pyplot as plt
from scipy import integrate, constants
import pandas as pd

df = pd.read_excel(r'res.xlsx')
# данные
m0 = 28000 #масса без топлива
M = 63150  # масса с топливом
Cf = 0.5 #сопротивление
ro = 1.293  # плотность воздуха
S = constants.pi * ((0.7 / 2) ** 2) #площадь сечения
g = constants.g
F = [1579000, 588000]

speed = []

def dv_dt(t, v):
    if t < 16:
        return 0
    if t < 90:
        M = 63150
        m0 = 28000
        Ft = F[0]
        k = (M - m0) / (4.66 * 60)
        return ((Ft / (M - k * t)) - ((Cf * ro * S) / (2 * (M - k * t))) * v ** 2 - g)
    if t < 305:
        M = 42000
        m0 = 16000
        Ft = F[1]
        k = (M - m0) / (5.2 * 60)
        return ((Ft / (M - k * t)) - ((Cf * ro * S) / (2 * (M - k * t))) * v ** 2 - g)


v0 = 0

t = np.linspace(0, 315, 375)

solve = integrate.solve_ivp(dv_dt, t_span=(0, max(t)), y0=[v0], t_eval=t)

x = solve.t
y = solve.y[0]


x2 = df['speed'].values
y2 = [i for i in range(0, len(x2))]
fig, p = plt.subplots()
p.plot(x, y, '-r', label="v(t) матмодель")
p.plot(x, [x2[i] for i in range(0, len(x2), 4)], '-b', label="v(t) ksp")
plt.legend()
plt.grid(True)
plt.show()