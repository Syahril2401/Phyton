import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d

# Data Eksperimen
suhu_data = np.array([10, 15, 20, 25, 30])
polutan_data = np.array([2.5, 2.1, 1.8, 1.3, 1.1])

# Fungsi Interpolasi linear
# 'kind='linear'' secara default sudah linear, tapi ditulis untuk kejelasan.
f_interp = interp1d(suhu_data, polutan_data, kind='linear')

# Estimasi kadar polutan
suhu_estimasi = 22
polutan_estimasi = f_interp(suhu_estimasi)

print(f"--- Estimasi Kadar Polutan ---")
print(f"Pada suhu {suhu_estimasi}°C, kadar polutan diestimasi sebesar: {polutan_estimasi:.3f} mg/L")

# grafik Scatter titik data dan garus interpolasi
plt.figure(figsize=(10, 7))

# plot titik data asli (scatter plot)
plt.scatter(suhu_data, polutan_data, color='blue', label='Data Eskperimen', zorder = 5, s=80)

# buat titik data asli (scatter plot)
plt.scatter(suhu_data, polutan_data, color='blue', label='Data Eksperimen', zorder=5, s=80)

# rentang suhu yg lebih halus utk menggambarkan garis interpolasi
suhu_garis = np.linspace(min(suhu_data), max(suhu_data), 500)
polutan_garis = f_interp(suhu_garis)

# plot garis interpolasi
plt.plot(suhu_garis, polutan_garis, color='red', linestyle='-', label='Interpolasi Linear', linewidth=2)

# tampilkan nilai interpolasi pada suhu 22°C pada grafik
plt.plot(suhu_estimasi, polutan_estimasi, 'o', color='green', markersize=10, label=f'Estimasi pada {suhu_estimasi}°C ({polutan_estimasi:.3f} mg/L)', zorder=6)
plt.axvline(suhu_estimasi, color='green', linestyle='--', linewidth=0.7)
plt.axhline(polutan_estimasi, color='green', linestyle='--', linewidth=0.7)

# detail grafik
plt.title('Estimasi Kadar Polutan Berdasarkan Suhu (Interpolasi Linear)')
plt.xlabel('Suhu (°C)')
plt.ylabel('Kadar Polutan (mg/L)')
plt.grid(True, linestyle='--', alpha=0.7)
plt.legend()
plt.xticks(np.arange(min(suhu_data), max(suhu_data) + 1, 5)) # Set ticks x setiap 5
plt.ylim(0.5, 3.0) # Batasi rentang y untuk tampilan yang lebih baik
plt.tight_layout() # Menyesuaikan tata letak agar tidak terpotong
plt.show()