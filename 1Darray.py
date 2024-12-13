import numpy as np
#Create a 1D Array
x = np.array([1, 2, 3, 4, 5, 6])
print(x)
#Create a boolean array
x1 = ([1, 'hi', 0, False, True])
y = np.array(x, dtype = bool)
print(y)
#Extract items that satisfy a given condition
y1 = np.where(x > 1, x, np.nan)
print(y1)
#Extract items that satisfy a given condition with another value in numpy array
y2 = np.where(x > 2, 11, x)
print(y1)
#Extract items that satisfy a given condition with another value in numpy array without affecting orignal array
x2 = np.arange(15)
y3 = np.where(x2 > 8, 111, x2)
print("Orignal Array:", x2)
print("Replacing values greater than 8 with 111:\n", y3)
#Reshape an array
x3 = np.array([69, 420, 88, 8915, 228, 11])
y4 = x3.reshape(2, 3)
print(y4)
#Extract all numbers bw a given range from a numpy array
x4 = np.arange(50)
y5 = np.where((x4 > 20) & (x4 <= 45))
print(y5)
