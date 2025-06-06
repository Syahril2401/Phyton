import numpy as np
import matplotlib.pyplot as plt

# definisi fungsi suhu T(x)
def T(x):
    """
    Fungsi suhu air: T(x) = 25 + 5 * sin(x)
    x dalam jam (0 sampai 24).
    """
    return 25 + 5 * np.sin(x)

# definisi turunan eksak dT/dx
def dT_exact(x):
    """
    Turunan eksak dari T(x): dT/dx = 5 * cos(x)
    """
    return 5 * np.cos(x)

# impementasi turunan numerik (forward difference)
def forward_difference(func, x, h):
    """
    Menghitung turunan numerik menggunakan metode forward difference.
    f'(x) = (f(x + h) - f(x)) / h
    """
    return (func(x + h) - func(x)) / h

# parameter
x_range = np.linspace(0, 24, 100) # waktu dari 0 sampe 24 jam, dg 100 titik
h_step = 0.01 # ukuran langkah untuk turnan numerik (pilih kecil tapi tidak terlalu kcil)

print(f"--- Perhitungan Turunan Numerik dan Eksak ---")
print(f"Ukuran langkah (h) untuk forward difference: {h_step}")

# hitung turunan numerik untuk setiap titik di x_range
dT_numeric = forward_difference(T, x_range, h_step)

# hitung turunan eksak untuk setiap titik di x_range
dT_exact_values = dT_exact(x_range)

# menampilkan beberapa sampel hasil utk perbandingan
print("\nBeberapa Sampel Hasil:")
print(f"{'x (jam)':<10} | {'dT/dx Numerik':<18} | {'dT/dx Eksak':<15} | {'Selisih':<10}")
print("----------------------------------------------------------------------")
for i in range(0, len(x_range), len(x_range)//10): # Tampilkan setiap 10% data
    selisih = abs(dT_numeric[i] - dT_exact_values[i])
    print(f"{x_range[i]:<10.2f} | {dT_numeric[i]:<18.6f} | {dT_exact_values[i]:<15.6f} | {selisih:<10.6f}")

# perbandingan hasil dalam grafik
plt.figure(figsize=(12, 7))

# plot turunan eksak
plt.plot(x_range, dT_exact_values, label='Turunan Eksak: $5 \cos(x)$', color='blue', linewidth=2)

# plot turunan numerik
plt.plot(x_range, dT_numeric, label=f'Turunan Numerik (Forward Difference, h={h_step})', color='red', linestyle='--', linewidth=1.5)

# detail grafik
plt.title('Perbandingan Turunan Eksak dan Numerik (Forward Difference)')
plt.xlabel('Waktu (x) dalam Jam')
plt.ylabel('Kecepatan Perubahan Suhu (dT/dx)')
plt.grid(True, linestyle='--', alpha=0.7)
plt.legend()
plt.axhline(0, color='black', linestyle='-', linewidth=0.7) # Garis y=0
plt.xticks(np.arange(0, 25, 2)) # Ticks setiap 2 jam
plt.tight_layout()
plt.show()

# interpretasi singkat
print("\n--- Interpretasi ---")
print("Dari grafik dan sampel hasil, terlihat bahwa turunan numerik (forward difference)")
print(f"dengan ukuran langkah h={h_step} memberikan aproksimasi yang sangat baik")
print("terhadap turunan eksak.")
print("Perbedaan antara keduanya sangat kecil, menunjukkan akurasi metode numerik.")
print("Kecepatan perubahan suhu (dT/dx) berfluktuasi sepanjang hari,")
print("mengikuti pola sinusoidal (cosinus) yang menunjukkan kapan suhu meningkat atau menurun paling cepat.")
print("Ketika dT/dx positif, suhu meningkat. Ketika negatif, suhu menurun.")
print("Nilai absolut dT/dx tertinggi menunjukkan perubahan suhu tercepat.")