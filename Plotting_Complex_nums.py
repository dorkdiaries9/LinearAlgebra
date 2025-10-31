import matplotlib.pyplot as plt

x = int(input("Enter Real Part:"))
y = int(input("Enter imaginary Part:"))
z=complex(x,y)

def plot_complex(z,title):
    plt.plot([0,z.real],[0,z.imag])
    plt.xlabel("Real")
    plt.ylabel("Imaginary")
    plt.title(title)
    plt.grid = True
    plt.show()

def rotate_90(z):
    plot_complex(z*1j,"Rotated 90 degree")
def rotate_180(z):
    plot_complex(z*-1,"Rotated 180 degree")
def rotate_270(z):
    plot_complex(z*-1j,"Rotated 270 degree")

def scale(z,s):
    scaled_plot = z*s
    plot_complex(scaled_plot,f"scaled by {s}")

def plot_all_transformations(z):
    transformations = {
        "Original": z,
        "Rotate 90°": z*1j,
        "Rotate 180°": z*-1,
        "Rotate 270°": z*-1j,
        "Scaled 1/2": z*0.5,
        "Scaled 1/3": z*(1/3),
        "Scaled 2": z*2
    }
    plt.figure()
    for label, val in transformations.items():
        plt.plot([0, val.real], [0, val.imag], label=label)
    plt.xlabel("Real Axis")
    plt.ylabel("Imaginary Axis")
    plt.title("Complex Number Transformations")
    plt.legend()
    plt.grid(True)
    plt.axis("equal")
    plt.show()

while True:
    print("1.Original")
    print("2.Rotate by 90")
    print("3.Rotate by 180")
    print("4.Rotate by 270")
    print("5.Scalling by 1/2")
    print("6.Scalling by 1/3")
    print("7.Scalling by 2")
    print("8.exit")
    print("9. Show all transformations together")


    ch = int(input("Enter your choice:"))
    if ch == 1: plot_complex(z,"original")
    elif ch== 2: rotate_90(z)
    elif ch== 3: rotate_180(z)
    elif ch== 4: rotate_270(z)
    elif ch== 5: scale(z,1/2)
    elif ch== 6: scale(z,1/3)
    elif ch== 7: scale(z,2)
    elif ch== 8: break
    elif ch == 9: plot_all_transformations(z)
   

    else: print("Invalid choice")



    
    
        
