import numpy as np
import matplotlib.pyplot as plt

# definisi fungsi persamaan diferensial (ds/dt)
def f(t,s):
    """
    Fungsi yang mendefinisikan ODE: ds/dt = -0.5 * s
    """
    return -0.5 * s

# solusi eksak s(t)
def s_exact(t):
    """
    Solusi eksak dari ODE: s(t) = 10 * e^(-0.5 * t)
    """
    return 10 * np.exp(-0.5 * t)

# parameter utk metode euler
t_start = 0 # waktu awal
t_end = 10 # waktu akhir
h = 1     # ukuran langkah
s0 = 10 # kondisi awal

# array waktu diskrit
t = np.arange(t_start, t_end + h, h)
n_steps = len(t)

# array utk nyimpan hasil euler
s_euler = np.zeros(n_steps)
s_euler[0] = s0

print("--- Perhitungan Metode Euler vs Solusi Eksak ---")
print(f"Kondisi awal s(0) = {s0}")
print(f"Ukuran langkah (h) = {h}")
print(f"Rentang waktu: t = {t_start} sampai t = {t_end}") 
print("\nIterasi Euler:") 
print(f"{'t':<5} | {'s_Euler':<12} | {'s_Eksak':<12} | {'Error Abs':<12}") 
print("---------------------------------------------------------")
print(f"{t[0]:<5.1f} | {s_euler[0]:<12.6f} | {s_exact(t[0]):<12.6f} | {'-':<12}")

# implementasi metode euler
for i in range(n_steps - 1):
    s_euler[i+1] = s_euler[i] + h * f(t[i], s_euler[i])
    current_exact = s_exact(t[i+1])
    error_abs = abs(s_euler[i+1] - current_exact)
    print(f"{t[i+1]:<5.1f} | {s_euler[i+1]:<12.6f} | {current_exact:<12.6f} | {error_abs:<12.6f}") # Perbaikan format specifier

# hitung solusi eksak utk semua titik waktu
s_exact_values = s_exact(t)

# bandingkan hasil euler vs eksak dalam grafik
plt.figure(figsize=(12, 7))

# plot solusi eksak
plt.plot(t, s_exact_values, label='Solusi Eksak: $s(t) = 10e^{-0.5t}$', color='blue', linewidth=2) # Perbaikan 'labels' menjadi 'label'

# plot hasil metode euler
plt.plot(t, s_euler, 'ro--', label=f'Metode Euler (h={h})', markersize=6, linewidth=1)

# detail grafik
plt.title('Perbandingan Metode Euler dan Solusi Eksak untuk $ds/dt = -0.5s$')
plt.xlabel('Waktu (t)')
plt.ylabel('Kadar Polutan (s)') 
plt.grid(True, linestyle='--', alpha=0.7)
plt.legend()
plt.xticks(np.arange(t_start, t_end + 1, h))
plt.ylim(0, s0 + 2)
plt.tight_layout()
plt.show()

# interpretasi singkat
print("\n--- Interpretasi ---") 
print(f"Dari tabel dan grafik, terlihat bahwa Metode Euler dengan ukuran langkah h={h}")
print(f"mendekati solusi eksak. Namun, karena h yang relatif besar, ada perbedaan yang terlihat.") 
print(f"Metode Euler cenderung underestimated (nilai yang lebih rendah) dari solusi eksak karena") 
print(f"ia menggunakan slope dari awal interval dan mengasumsikan slope tersebut konstan")
print(f"sepanjang interval, padahal slope sebenarnya terus berubah (menurun) dalam kasus ini.")
print(f"Jika ukuran langkah 'h' diperkecil, aproksimasi Metode Euler akan menjadi lebih akurat.") 