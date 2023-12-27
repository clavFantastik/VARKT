import numpy as np
import matplotlib.pyplot as plt
from scipy import integrate, constants

# данные
m0 = 28000  # масса без топлива
M = 63150  # масса с топливом
Cf = 0.5  # сопротивление
ro = 1.293  # плотность воздуха
S = constants.pi * ((1.3 / 2) ** 2)  # площадь сечения
g = constants.g
F = [1571000, 388000]


def dv_dt(t, v):
    if t < 30:
        M = 63150
        m0 = 28000
        Ft = F[0]
        T = 4.66 * 60
        k = (M - m0) / T
        return ((Ft / (M - k * t)) + ((Cf * ro * S) / (2 * (M - k * t))) * v ** 2 - g)
    if t < 105:
        M = 40000
        m0 = 18000
        Ft = F[1]
        T = 5.17 * 60
        k = (M - m0) / T
        return ((Ft / (M - k * t)) + ((Cf * ro * S) / (2 * (M - k * t))) * v ** 2 - g)


v0 = 0

t = np.linspace(0, 300, 400) # 400 чисел, равномерно распределенных между 0 и 300

solve = integrate.solve_ivp(dv_dt, t_span=(0, max(t)), y0=[v0], t_eval=t)

x = solve.t
y = solve.y[0]

plt.figure(figsize=(8, 8))
plt.plot(x, y, '-r', label="v(t)")
plt.legend()
plt.grid(True)
plt.show()
