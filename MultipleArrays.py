import numpy as np
#stack 2 arrays vertically
x = np.array([[1, 2, 3], [4, 5, 6]])
y = np.array([[7, 8, 9], [10, 11, 12]])
z = np.vstack((x, y))
print(z)
#stack 2 arrays horitzontally 
z2 = np.hstack((x, y))
print(z2)
#Get the common elements bw 2 arrays
x1 = np.array([[1, 2, 3], [111, 222, 333]])
y1 = np.array([[1, 2, 3], [999, 777, 666]])
z3 = np.intersect1d(x, y)
print(z3)
#Remove elemetns in array that exist in another array
z4 = np.setdiff1d
print(z4)
#Get the position where elements of 2 Arrays match
z5 = np.where(x1 == y1)
print(z5)