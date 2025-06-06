import numpy as np
import matplotlib.pyplot as plt

# data eksperimen
suhu_data = np.array([10, 15, 20, 25, 30])
polutan_data = np.array([2.5, 2.1, 1.8, 1.3, 1.1])

print("--- Data Eksperimen ---")
for i in range(len(suhu_data)):
    print(f"Suhu: {suhu_data[i]}°C, Polutan: {polutan_data[i]} mg/L")

# Regresi Linear (metode least squares)
coefficients = np.polyfit(suhu_data, polutan_data, 1)
a = coefficients[0] 
b = coefficients[1]

# Persamaan garis regresi y = ax +b
print("\n--- Hasil Regresi Linear ---")
print(f"Koefisien a (slope): {a:.4f}")
print(f"Koefisien b (intercept): {b:.4f}")
print(f"Persamaan Garis Regresi: y = {a:.4f}x + {b:.4f}")

# Grafik data titik dan garis regesi
plt.figure(figsize=(10, 7))

# plot titik data asli (scatter plot)
plt.scatter(suhu_data, polutan_data, color='blue', label='Data Eksperimen', zorder=5, s=80)

x_regresi = np.array([min(suhu_data), max(suhu_data)])
y_regresi = a * x_regresi + b

# plot garis regresi
plt.plot(x_regresi, y_regresi, color='red', linestyle='-', label=f'Garis Regresi: y = {a:.4f}x + {b:.4f}', linewidth=2)

# detail grafik
plt.title('Regresi Linear Hubungan Suhu dan Kadar Polutan')
plt.xlabel('Suhu (°C)')
plt.ylabel('Kadar Polutan (mg/L)')
plt.grid(True, linestyle='--', alpha=0.7)
plt.legend()
plt.xticks(np.arange(min(suhu_data), max(suhu_data) + 1, 5)) # Set ticks x setiap 5
plt.ylim(0.5, 3.0) # Batasi rentang y agar grafik terlihat lebih baik
plt.tight_layout()
plt.show()

# interpretasi tren
print("\n--- Interpretasi Tren ---")
if a < 0:
    print(f"Koefisien 'a' (slope) adalah {a:.4f}, yang bernilai negatif.")
    print("Ini menunjukkan bahwa terdapat tren bahwa kadar polutan CENDERUNG MENURUN seiring dengan kenaikan suhu air.")
elif a > 0:
    print(f"Koefisien 'a' (slope) adalah {a:.4f}, yang bernilai positif.")
    print("Ini menunjukkan bahwa terdapat tren bahwa kadar polutan CENDERUNG MENINGKAT seiring dengan kenaikan suhu air.")
else:
    print(f"Koefisien 'a' (slope) adalah {a:.4f}, yang bernilai nol atau sangat dekat nol.")
    print("Ini menunjukkan bahwa tidak ada hubungan linear yang signifikan antara suhu dan kadar polutan, atau kadar polutan relatif stabil.")
