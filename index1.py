def produksi(x):
    """
    Menghitung estimasi jumlah produksi tas berdasarkan model polinomial orde 4.

    Parameter:
        x (int or float): Bulan ke-x (1 <= x <= 144)
        
    Returns:
        float: Estimasi jumlah produksi
    """
    return 1937.026 + 22.006 * x + 0.642 * x**2 - 0.00445 * x**3 + 0.0000287 * x**4


# Contoh penggunaan fungsi:
if __name__ == "__main__":
    # Hitung estimasi produksi untuk bulan ke-100
    bulan = 100
    estimasi = produksi(bulan)
    print(f"Estimasi produksi tas pada bulan ke-{bulan} adalah: {estimasi:.3f} unit")
