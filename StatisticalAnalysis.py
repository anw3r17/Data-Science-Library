import numpy as np
import random
#find mean, median, standard deviation of numpy array
x = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
m = np.mean(x)
mm = np.median(x)
st = np.std(x)
print(m)
print(mm)
print(st)
#find the percentile scores of numpy array
x1 = np.percentile(x, [25, 50, 75])
print("25th, 50th and 75th percentile of the array is:\n", x1)
#compute the eucledian distance bw two numpy arrays
x2 = np.array([1, 2, 3, 4])
y2 = np.array([5, 6, 7, 8])
z = np.linalg.norm(x2 - y2)
print(z)
#find correlation between two columns of a numpy array
x3 = np.random.randint(0, 100, 500)
y3 = x3 + np.random.randint(0, 100, 500)
corr = np.corrcoef(x3, y3)
print(corr)
#probalistic sampling
k = np.array([1, 2, 3, 4, 5, 6])
k1 = np.random.choice(k, size = 3, replace = True, p = [0.1, 0.1, 0.2, 0.3, 0.2, 0.2])
print(k1)
#compute moving average
l = np.random.randint(10, size = 10)
movavg = np.convolve(l, np.ones(3)/3, mode = 'valid')
print(l)
print(movavg)