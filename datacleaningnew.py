import numpy as np
#missing values find numpy artay
x = np.array([[1, 2, np.nan], [4, 5, 6], [np.nan, np.nan, 9]])
print("Original array:\n", x)
y = np.argwhere(np.isnan(x))
print("mising values:\n", y)
#drop rows that contain a missing value 
x1 = np.isnan(x).any(axis = 1)
x2 = x[~x1]
print("Array after dropping missing rows:\n", x2)
#replace missing values with 0
x[np.isnan(x)] = 0
print("Replacing missing values with 0:\n")
print(x)
#drop all missing values from the numpy array
x1 = np.array([[1, 2, np.nan], [4, 5, 6], [np.nan, np.nan, 9]])
print("\n", x1)
non = x1[~np.isnan(x1)]
print("dropping missing values:\n")
print(non)