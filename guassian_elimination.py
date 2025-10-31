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

n = int(input("Enter number of equations: "))
print("Enter coefficients row-wise:")
A = np.array([list(map(float, input().split())) for _ in range(n)])
b = np.array(list(map(float, input("Enter constants: ").split())))

print("\nRow Echelon Form using gaussian elimination:", gaussian_elimination(A, b))
