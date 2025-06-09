import numpy as np
import matplotlib.pyplot as plt

# ODE
f = lambda t, s: t

# Ukuran langkah
h = 0.1
t = np.arange(0, 1 + h, h)

# nilai awal: f(0) = 0
s0 = 0

# Array utk menyimpan hasil Euler
s = np.zeros(len(t))
s[0] = s0

# Metode Euler
for i in range(len(t) - 1):
    s[i + 1] = s[i] + h * f(t[i], s[i])

# Plot hasil Euler dan solusi eksak
plt.figure(figsize=(12, 8))
plt.plot(t, s, 'bo--', label='Approximate (Euler)') # Perbaikan di sini
plt.plot(t, 0.5 * t**2, 'g', label='Exact')
plt.title('Approximate and Exact Solution \n for df/dt = t with f(0) = 0')
plt.xlabel('t')
plt.ylabel('f(t)')
plt.grid()
plt.legend(loc='lower right')
plt.show()

