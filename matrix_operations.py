#Matrix addition multiplication subtraction and inverse

import numpy as np

def get_matrix():
    rows = int(input("Enter number of rows: "))
    cols = int(input("Enter number of columns: "))
    elements = input("Enter matri elements separated by spaces:").split()
    matrix = np.array(elements,dtype=float).reshape(rows,cols)
    return matrix
def add_matrix(m1,m2):
    print("Addition of Matrices:",np.add(m1,m2))
def sub_matrix(m1,m2):
    print("Subtraction of Matrices:",np.subtract(m1,m2))
def mul_matrix(m1,m2):
    print("Multiplication of Matrices:",np.matmul(m1,m2))
def invertible_matrix():
    input_matrix = get_matrix()
    if input_matrix.shape[0]==input_matrix.shape[1]:
        det = np.linalg.det(input_matrix)
        if det !=0:
            print("Matrix invertible:",np.linalg.inv(input_matrix))
        else:
            print("Determinat not = 0 not invertible")
    else:
        print("rows and cols not equal cant be invertible")
print("Enter matrix 1")
m1 = get_matrix()
print("Enter matrix 2")
m2 = get_matrix()
    
while True:
    print("1. ADD MATRICES")
    print("2. SUBTRACT MATRICES")
    print("3. MULTIPLY MATRICES (element-wise)")
    print("4. CHECK INVERTIBILITY AND FIND INVERSE")
    print("5. EXIT PROGRAM")

    ch = int(input("Enter your choice:"))

    if ch == 1:
        add_matrix(m1,m2)
    elif ch == 2:
        sub_matrix(m1,m2)
    elif ch == 3:
        mul_matrix(m1,m2)
    elif ch == 4:
        invertible_matrix()
    elif ch == 5:
        print("exiting program...")
    
    else:
        print("Enter a valid choice")
    
    
    
    
    
    
