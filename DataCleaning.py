import numpy as np
#find position of missing values in numpy array
x = np.array([[1, 2, 3], [4, 5, np.nan]])
y = np.argwhere(np.isnan(x))
print(y)
#drop rows that contain a missing value from a numpy array
k = np.array([[1, np.nan, 3], [np.nan, 5, 6], [7, np.nan, np.nan]])
k1 = ~np.isnan(k).any(axis = 1)
clean = k[k1]
print(clean)
#replace missing values with 0
k[~np.isnan(k)] = 0
print(k)
#drop all missing values from the numpy array
non = k[~np.isnan(k)]
print(non)