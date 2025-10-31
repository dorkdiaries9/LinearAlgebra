import numpy as np

def gram_schmidt(V):
    # Validate matrix dimensions (all vectors must have same length)
    m = len(V[0])
    if any(len(row) != m for row in V):
    raise ValueError("All rows must have the same number of columns")
    
    U = []
    for v in V:
        for u in U:
            v -= np.dot(v, u) / np.dot(u, u) * u
        U.append(v)
    return [u / np.linalg.norm(u) for u in U]

V = [np.array([1, 1, 0], float), np.array([1, 0, 1], float)]
U = gram_schmidt(V)
for i, u in enumerate(U, 1):
    print(f"u{i} =", np.round(u, 3))
