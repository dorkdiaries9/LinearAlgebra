import numpy as np

def gram_schmidt(V):
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
