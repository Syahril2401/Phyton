import numpy as np
import matplotlib.pyplot as plt

#  Definisikan Fungsi P(x) dan Turunannya P'(x)
def P(x):
    return x**3 - 4*x**2 + 6*x - 24

def dP(x):
    return 3*x**2 - 8*x + 6

# Implementasi Metode Bisection yang Lebih Ringkas 
def bisection_method_simple(func, a, b, tol=1e-7, max_iter=100):
    if func(a) * func(b) >= 0:
        
        return None, None, None 

    for _ in range(max_iter):
        c = (a + b) / 2
        if func(c) == 0 or (b - a) / 2 < tol:
            return c, (b - a) / 2 
        elif func(a) * func(c) < 0:
            b = c
        else:
            a = c
    return (a + b) / 2, (b - a) / 2

# Implementasi Metode Newton-Raphson yang Lebih Ringkas 
def newton_raphson_method_simple(func, dfunc, x0, tol=1e-7, max_iter=100):
    x_n = x0
    for _ in range(max_iter):
        fxn = func(x_n)
        dfxn = dfunc(x_n)

        if dfxn == 0:
            return None, None 

        x_next = x_n - fxn / dfxn
        error = abs(x_next - x_n)
        if error < tol:
            return x_next, error 
        x_n = x_next
    return x_n, error 

# Eksekusi dan Tampilkan Hasil Ringkas

tolerance = 1e-7

print("===================================")
print("Pencarian Akar P(x) = x^3 - 4x^2 + 6x - 24")
print("===================================")

# Metode Bisection
print("\n--- Metode Bisection ---")
bisection_a = 3
bisection_b = 5
root_bisection, error_bisection = bisection_method_simple(P, bisection_a, bisection_b, tol=tolerance)

if root_bisection is not None:
    print(f"Akar ditemukan: {root_bisection:.7f}")
    print(f"Estimasi error: {error_bisection:.7f}")
else:
    print("Metode Bisection gagal menemukan akar.")

# Metode Newton-Raphson
print("\n--- Metode Newton-Raphson ---")
newton_x0 = 3.5
root_newton, error_newton = newton_raphson_method_simple(P, dP, newton_x0, tol=tolerance)

if root_newton is not None:
    print(f"Akar ditemukan: {root_newton:.7f}")
    print(f"Estimasi error: {error_newton:.7f}")
else:
    print("Metode Newton-Raphson gagal menemukan akar.")

# Visualisasi Grafik yang Lebih Ringkas 
plt.figure(figsize=(10, 6))
x_plot = np.linspace(0, 5, 500)
plt.plot(x_plot, P(x_plot), label='P(x) = $x^3 - 4x^2 + 6x - 24$', color='blue')
plt.axhline(0, color='black', linestyle='--', linewidth=0.8)

# Tandai akar yang berhasil ditemukan
if root_bisection is not None:
    plt.plot(root_bisection, P(root_bisection), 'ro', markersize=10, label=f'Akar Bisection ({root_bisection:.4f})')
    plt.axvline(root_bisection, color='red', linestyle=':', linewidth=0.7)

if root_newton is not None:
    plt.plot(root_newton, P(root_newton), 'go', markersize=10, label=f'Akar Newton-Raphson ({root_newton:.4f})')
    plt.axvline(root_newton, color='green', linestyle=':', linewidth=0.7)

plt.title('Grafik Fungsi P(x) dan Titik Akar')
plt.xlabel('x')
plt.ylabel('P(x)')
plt.grid(True)
plt.legend()
plt.ylim(-30, 40)
plt.show()