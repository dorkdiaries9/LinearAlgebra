import numpy as np

def input_vector():
    dim = int(input("Enter dimension of vector:"))
    vec = []
    for i in range(dim):
        val = int(input("Enter value:"))
        vec.append(val)
    return np.array(vec)

print("Enter Vector u :")
u = input_vector()
print("Enter Vector v :")
v = input_vector()

if u.shape != v.shape:
    print("Vectors must have same dimension")
    exit()

while True:
    print("1.Compute au + bv")
    print("2.Compute dot product")
    print("3.exit")

    ch = int(input(" Enter your choice : "))
    if ch == 1:
        a = int(input("Enter scaler a :"))
        b = int(input("Enter scaler b :"))
        result = a*u + b*v
        print("au+bv=",result)
    elif ch == 2:
        dot = np.dot(u,v)
        print("Dot product",dot)
    else:
        print('invalid choice!')
    

