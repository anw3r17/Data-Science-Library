import numpy as np
#normazlize array so that values range exatcly bw 0 & 1
x = np.array([1, 2, 3, 4, 5, 6])
min_v = np.min(x)
max_v = np.max(x)
norm = (x - min_v) / (max_v - min_v)
print(norm)
#compute max by min for 2d array
x1 = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
min_v2 = np.min(x1, axis = 1)
max_v2 = np.max(x1, axis = 1)
minbymax = min_v2 / max_v2
print(minbymax)