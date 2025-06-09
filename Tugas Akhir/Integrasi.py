import numpy as np
import matplotlib.pyplot as plt

# definisi fungsi polutan P(x) - Dikoreksi ke P(x) agar konsisten dengan plotting
def P(x):
    """
    Fungsi kadar polutan: P(x) = 2 + sin(x / 24 * 2pi)
    x dalam jam (0 sampai 24).
    """
    return 2 + np.sin(x / 24 * 2 * np.pi)

# batas integrasi
a = 0
b = 24

# jumlah subinterval
n_intervals = 1000 
delta_x = (b - a) / n_intervals

# buat titik diskrit utk perhitungan
x_points = np.linspace(a, b, n_intervals + 1)

# hitung polutan pada setiap titik
y_points = P(x_points) 

# --- Perhitungan Akumulasi Polutan ---
print("--- Perhitungan Akumulasi Polutan (Integral Numerik) ---")
print(f"Jumlah subinterval (n): {n_intervals}")
print(f"Ukuran langkah (delta_x): {delta_x:.4f}")

# a. Riemann Sum (Left) - KOREKSI RUMUS DAN PENGGUNAAN VARIABEL
integral_lrs = np.sum(y_points[:-1] * delta_x)
print(f"\nRiemann Sum (Left): {integral_lrs:.6f}")

# b. Riemann Sum (Right)
integral_rrs = np.sum(y_points[1:] * delta_x)
print(f"Riemann Sum (Right): {integral_rrs:.6f}")

# c. Riemann Sum (Midpoint) - PASTIKAN PERHITUNGAN X_MIDPOINTS DAN Y_MIDPOINTS DI SINI
x_midpoints = (x_points[:-1] + x_points[1:]) / 2
y_midpoints = P(x_midpoints) 
integral_mrs = np.sum(y_midpoints * delta_x)
print(f"Riemann Sum (Midpoint): {integral_mrs:.6f}")

# d. Trapezoidal Rule (menggunakan implementasi manual)
integral_trap_manual = (delta_x / 2) * (y_points[0] + 2 * np.sum(y_points[1:-1]) + y_points[-1])
print(f"Trapezoidal Rule (Manual): {integral_trap_manual:.6f}")

# Integral Eksak (dari perhitungan analitis)
integral_exact = 48.0
print(f"\nIntegral Eksak (Referensi): {integral_exact:.6f}")

# bandingkan semua hasil dan mana yg paling mendekati eksak
print("\n--- Perbandingan dan Analisis Error ---")
methods = {
    "Riemann (Left)": integral_lrs,
    "Riemann (Right)": integral_rrs,
    "Riemann (Midpoint)": integral_mrs,
    "Trapezoidal Rule (Manual)": integral_trap_manual 
}

# hitung error absolut
errors = {name: abs(value - integral_exact) for name, value in methods.items()}

# cari metode dengan error terkecil
best_method = min(errors, key=errors.get)

for name, value in methods.items():
    print(f"{name:<25}: {value:.6f} (Error: {errors[name]:.6f})")

print(f"\nMetode yang paling mendekati eksak adalah: {best_method} (Error: {errors[best_method]:.6f})")

# --- Visualisasi Grafik ---
plt.figure(figsize=(12, 7))

# plot fungsi polutan
x_plot = np.linspace(a, b, 500) # Lebih banyak titik untuk kurva halus
y_plot = P(x_plot) # Menggunakan P(x) yang sudah didefinisikan
plt.plot(x_plot, y_plot, color='blue', label='P(x) = $2 + \sin(x/24 \cdot 2\pi)$', linewidth=2)

plt.fill_between(x_points, 0, y_points, color='lightblue', alpha=0.6, label='Area Akumulasi Polutan')

# detail grafik
plt.title('Total Akumulasi Polutan Selama 24 Jam')
plt.xlabel('Waktu (x) dalam Jam')
plt.ylabel('Kadar Polutan (mg/L)')
plt.grid(True, linestyle='--', alpha=0.7)
plt.legend()
plt.xticks(np.arange(0, 25, 2)) # Ticks setiap 2 jam
plt.ylim(0, 3.5) 
plt.tight_layout()
plt.show()