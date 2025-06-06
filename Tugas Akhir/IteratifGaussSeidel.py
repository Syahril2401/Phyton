import numpy as np

# Fungsi untuk Metode Gauss-Seidel
def gauss_seidel(A, b, initial_guess, tol=0.01, max_iter=100):
    n = len(b)
    x = initial_guess.copy() # Nilai x, y, z saat ini
    x_prev = initial_guess.copy() # Nilai x, y, z dari iterasi sebelumnya
    iterations = 0

    print("\n--- Implementasi Metode Gauss-Seidel ---")
    print(f"Toleransi error: {tol}")
    print(f"Iterasi | x_k       | y_k       | z_k       | Max Error")
    print("-----------------------------------------------------------------")
    print(f"0       | {x_prev[0]:<9.6f} | {x_prev[1]:<9.6f} | {x_prev[2]:<9.6f} | -")

    for k in range(max_iter):
        iterations += 1
        x_prev[:] = x[:] # Simpan nilai dari iterasi sebelumnya untuk perhitungan error

        # Persamaan 1 utk x
        x[0] = (b[0] - A[0,1]*x[1] - A[0,2]*x[2]) / A[0,0]

        # Persamaan 2 utk y
        x[1] = (b[1] - A[1,0]*x[0] - A[1,2]*x[2]) / A[1,1]

        # Persamaan 3 utk z
        x[2] = (b[2] - A[2,0]*x[0] - A[2,1]*x[1]) / A[2,2]

        # Hitung error (norma perbedaan antara iterasi sekarang dan sebelumnya)
        # Menggunakan norma tak hingga (max(|x_k - x_k-1|))
        max_error = np.max(np.abs(x - x_prev))

        print(f"{iterations:<7d} | {x[0]:<9.6f} | {x[1]:<9.6f} | {x[2]:<9.6f} | {max_error:<9.6f}")

        if max_error < tol:
            print("\nKonvergen!")
            return x, iterations, True # Mengembalikan solusi, jumlah iterasi, dan status konvergensi

    print(f"\nTidak konvergen dalam {max_iter} iterasi. Error terakhir: {max_error:.6f}")
    return x, iterations, False # Mengembalikan solusi terakhir, jumlah iterasi, dan status non-konvergen

# Matriks A dan B
A = np.array([[3, 2, 1],
              [2, 3, 3],
              [5, 2, 4]])

B = np.array([10, 13, 20])

# Tebakan awal (biasanya 0,0,0)
initial_guess = np.array([0.0, 0.0, 0.0])
tolerance = 0.01
max_iterations_gauss = 100

solution_gauss, num_iterations, converged = gauss_seidel(A, B, initial_guess, tol=tolerance, max_iter=max_iterations_gauss)

if converged:
    print(f"\nSolusi akhir dari Metode Gauss-Seidel: x = {solution_gauss[0]:.6f}, y = {solution_gauss[1]:.6f}, z = {solution_gauss[2]:.6f}")
else:
    print(f"\nMetode Gauss-Seidel tidak konvergen ke toleransi {tolerance} dalam {max_iterations_gauss} iterasi.")
    print(f"Solusi terakhir: x = {solution_gauss[0]:.6f}, y = {solution_gauss[1]:.6f}, z = {solution_gauss[2]:.6f}")