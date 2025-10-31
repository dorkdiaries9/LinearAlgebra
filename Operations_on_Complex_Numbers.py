#complex numbers operations
def add(x,y,a,b):
    print("Addition: ",complex(x,y)+complex(a,b))
def sub(x,y,a,b):
    print("Subtraction: ",complex(x,y)- complex(a,b))
def multi(x,y,a,b):
    print("Multiplication: ",complex(x,y)*complex(a,b))
def div(x,y,a,b):
    print("Division: ",complex(x,y)/complex(a,b))
def multiply_conjugate(x,y):
    complex_number = complex(x,y)
    conj = complex_number.conjugate()
    print("Multiplication with conjugate: ",complex_number*conj)

while True:
    print("1.Add two complex numbers")
    print("2.Subtract two complex numbers")
    print("3.Multiply two complex numbers")
    print("4.Divide two complex numbers")
    print("5.Multipy complex number with its conjugate")
    print("6.Exit")

    ch = int(input("Enter Choice:"))
    if ch == 6:
        print("Exiting program...")
        break
    x = int(input("x:"))
    y = int(input("y:"))
    if ch in [1,2,3,4]:
        a = int(input("a:"))
        b = int(input("b:"))
    
    if ch==1:
        add(x,y,a,b)
    elif ch==2:
        sub(x,y,a,b)
    elif ch==3:
        multi(x,y,a,b)
    elif ch==4:
        div(x,y,a,b)
    elif ch==5:
        multiply_conjugate(x,y)
    else:
        print("Enter a valid choice!")
