#eigen values and eigen vectors

import numpy as np
from numpy.linalg import eig

M = np.array[[1,2,3],[4,5,6],[7,8,9]]
w,v = eig(M)
print("EIGEN VALUE",w)
print("EIGEN VECTOR",v)
