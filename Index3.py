
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.optimize import brentq

# ========================
# SOAL 1 - MODEL POLINOMIAL
# ========================
# Fungsi untuk membaca data dan membangun model
def build_polynomial_model(file_path):
    data = pd.read_csv(file_path)
    x = np.arange(1, len(data) + 1)
    y = data["produksi"].values

    # Fit model polinomial orde 4
    coeffs = np.polyfit(x, y, 4)
    model = np.poly1d(coeffs)

    return model, x, y

# ========================
# SOAL 2 - KONVERSI KE FUNGSI NUMERIK
# ========================
# Fungsi numerik dari model (koefisien diambil dari hasil polyfit)
def produksi(x):
    return 1937.026 + 22.006 * x + 0.642 * x**2 - 0.00445 * x**3 + 0.0000287 * x**4

# ========================
# SOAL 3 - PREDIKSI GUDANG
# ========================
# Fungsi selisih antara produksi dan kapasitas gudang
def selisih(x):
    return produksi(x) - 25000

def prediksi_gudang():
    # Cari akar fungsi (bulan saat produksi melebihi 25.000 tas)
    bulan_melebihi = int(brentq(selisih, 100, 200))
    bulan_mulai_bangun = bulan_melebihi - 13

    print(f"Produksi melebihi 25.000 pada bulan ke-{bulan_melebihi}")
    print(f"EIGER harus mulai membangun gudang baru pada bulan ke-{bulan_mulai_bangun}")


if __name__ == "__main__":
    
    model, x, y = build_polynomial_model("aol_data(in).csv")

    # Plot model dan data
    x_pred = np.linspace(1, len(x), 500)
    y_pred = model(x_pred)

    plt.figure(figsize=(10, 6))
    plt.plot(x, y, 'o', label='Data Asli')
    plt.plot(x_pred, y_pred, '-', label='Model Polinomial Orde 4')
    plt.xlabel('Bulan ke-x')
    plt.ylabel('Jumlah Produksi')
    plt.title('Model Tren Produksi Tas')
    plt.legend()
    plt.grid(True)
    plt.savefig("hasil_model_soal1.png")
    plt.close()

    # Jalankan prediksi soal 3
    prediksi_gudang()
