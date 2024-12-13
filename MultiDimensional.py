import numpy as np
#convert an array of arrays into flat 1d
x = np.array([[1, 2, 3], [4, 5, 6]])
x1 = x.flatten()
print(x1)
#swap two columns in a 2d numpy array
x2 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
x2[:, [0, 2]] = x2[:, [2, 0]]
print(x2)