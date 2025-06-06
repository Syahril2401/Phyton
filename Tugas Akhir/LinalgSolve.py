import numpy as np

# matriks koefisien A
A = np.array([[3, 2, 1],
              [2, 3, 3],
              [5, 2, 4]])

# vektor konstanta B
B = np.array([10, 13, 20])

print("Solusi menggunakan numpy.linalg.solve")
try:
    # menggunakan np.linalg.solve untuk menemukan solusi X
    X_numpy = np.linalg.solve(A,B)
    print(f"Solusi (x, y, z) dari numpy.linalg.solve: {X_numpy}")
    print(f"x = {X_numpy[0]:.6f}")
    print(f"x = {X_numpy[1]:.6f}")
    print(f"x = {X_numpy[2]:.6f}")

    # verifikasi solusi
    print("\nVerifikasi Solusi:")
    print(f"Persamaan 1: 3*{X_numpy[0]:.6f} + 2*{X_numpy[1]:.6f} + 1*{X_numpy[2]:.6f} = {3*X_numpy[0] + 2*X_numpy[1] + X_numpy[2]:.6f} (Target: 10)")
    print(f"Persamaan 2: 2*{X_numpy[0]:.6f} + 3*{X_numpy[1]:.6f} + 3*{X_numpy[2]:.6f} = {2*X_numpy[0] + 3*X_numpy[1] + 3*X_numpy[2]:.6f} (Target: 13)")
    print(f"Persamaan 3: 5*{X_numpy[0]:.6f} + 2*{X_numpy[1]:.6f} + 4*{X_numpy[2]:.6f} = {5*X_numpy[0] + 2*X_numpy[1] + 4*X_numpy[2]:.6f} (Target: 20)")

except np.linalg.LinAlgError as e:
    print(f"Error: {e}. Sistem persamaan mungkin singular atau tidak memiliki solusi unik.")