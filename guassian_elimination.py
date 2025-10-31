import numpy as np

def gaussian_elimination(A, b):
    A = A.astype(float)
    n = len(b)
    for i in range(n):
        if A[i, i] == 0:
            A[[i, i+1]] = A[[i+1, i]]  # Swap rows if pivot is zero
        for j in range(i+1, n):
            ratio = A[j, i] / A[i, i]
            A[j] -= ratio * A[i]
            b[j] -= ratio * b[i]
    return np.column_stack((A, b))

A = np.array([[2, 1, -1], [-3, -1, 2], [-2, 1, 2]], float)
b = np.array([8, -11, -3], float)
print("Row Echelon Form:\n", gaussian_elimination(A, b))
