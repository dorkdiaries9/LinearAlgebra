#projection of u on v and v on u
import numpy as np
def get_vector():
    dim = int(input("Enter dimension of vectors:"))
    vect=[]
    for i in range(dim):
        val = int(input("enter the value:"))
        vect.append(val)
    return np.array(vect)

u = get_vector()
v = get_vector()
dot_prod = np.dot(u,v)

v_mag_sq = np.dot(v,v)
u_mag_sq = np.dot(u,u)

proj_u_on_v = (dot_prod/v_mag_sq)*v
proj_v_on_u = (dot_prod/u_mag_sq)*u


print("Projection of u on v:", proj_u_on_v)
print("Projection of v on u:", proj_v_on_u)
