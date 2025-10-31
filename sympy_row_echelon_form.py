#row echelon form of a matrix
import numpy as np
import sympy

def get_matrix():
    rows=int(input("Enter number of rows:"))
    cols=int(input("Enter number of cols:"))
    elem=input("Enter elements separated by spaces").split()
    matrix=np.array(elem,dtype=float).reshape(rows,cols)
    return matrix

M = get_matrix()
sym_matrix = sympy.Matrix(M)
ref=sym_matrix.echelon_form()
rref, pivots = sym_matrix.rref() 
rank=sym_matrix.rank()

print("Reduced Row Echelon Form (RREF):")  # Display RREF
sympy.pprint(rref)

print("Pivot Columns: ", pivots)


print("Reduced Echelon form (REF):",ref)
print("rank of Matrix : ",rank)
