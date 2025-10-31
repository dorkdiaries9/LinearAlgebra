def determinant(mat):
    if len(mat) == 1:
        return mat[0][0]
    if len(mat) == 2:
        return mat[0][0]*mat[1][1] - mat[0][1]*mat[1][0]
    return sum((-1)**c * mat[0][c] * determinant([r[:c] + r[c+1:] for r in mat[1:]]) for c in range(len(mat)))

A = [[2, 5, 3],
     [1, -2, -1],
     [1, 3, 4]]

print("Determinant:", determinant(A))
