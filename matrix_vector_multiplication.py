#Matrix Vector and vector matrix multiplication
import numpy as np

def get_matrix():
    rows = int(input("Enter number of rows:"))
    cols = int(input("Enter number of cols:"))
    elements = input("Enter elements separated by spaces").split()
    matrix = np.array(elements,dtype=float).reshape(rows,cols)
    return(matrix)
def get_vector():
    dim = int(input("Enter dimension of vector"))
    vect=[]
    for i in range(dim):
        val=int(input("Enter value"))
        vect.append(val)
    return np.array(vect)

while True:
    print("1.Matrix x Vector")
    print("2.Vector x Matrix")
    print("3.Exit")
    ch = int(input("Enter your choice:"))
    M = get_matrix()
    V = get_vector()
    if ch == 1:
        
        if M.shape[1]==V.shape[0]:
            result=M.dot(V)
            print(result)
        else:
            print("columns of matrix must be equal to vector dimension")
    elif ch == 2:
        
        if V.shape[0]==M.shape[0]:
            result=V.dot(M)
            print(result)
        else:
            print("rows of matrix must be equal to vector dimension")
    elif ch == 3:
        print("Exiting")
        exit()
    else:
        print("Invalid choice")
        

        
    
        
        

