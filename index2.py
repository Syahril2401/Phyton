from scipy.optimize import brentq

# Definisikan fungsi produksi
def produksi(x):
    return 1937.026 + 22.006 * x + 0.642 * x**2 - 0.00445 * x**3 + 0.0000287 * x**4

# Fungsi selisih antara produksi dan batas gudang
def selisih(x):
    return produksi(x) - 25000

# Cari akar antara bulan ke-100 hingga 200 (karena setelah 100 produksi mulai tinggi)
akar = brentq(selisih, 100, 200)

bulan_melebihi = int(akar)
bulan_mulai_bangun = bulan_melebihi - 13

print(f"Produksi melebihi 25.000 pada bulan ke-{bulan_melebihi}")
print(f"EIGER harus mulai membangun gudang baru pada bulan ke-{bulan_mulai_bangun}")
