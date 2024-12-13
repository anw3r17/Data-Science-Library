import numpy as np
import pandas as pd # type: ignore
#get the minimum, max, median, 25th, 75th percentile of a numeric series
x = pd.Series(np.random.randint(500, size=20))
m = np.median(x)
mm = np.max(x)
mini = np.min(x)
p = np.percentile(x, 25)
pp = np.percentile(x, 75)
print(m)
print(mini)
print(mm)
print(p)
print(pp)
#get frequency counts of unique items of a series
x1 = pd.Series(np.random.randint(100, size=10))
print(x1)
freq = x1.value_counts()
print(freq)
#bin a numeric series to 10 groups of equal size
age = pd.Series(np.random.randint(0, 100, size = 10))
bin = [0, 18, 25, 35, 55, 75, 100]
lab = ['young', 'teen', 'young adult', 'adult', 'old', 'senior citizen']
b = pd.cut(age, bins = bin, labels = lab, right = False)
c = pd.concat([age, b], axis = 1)
c.columns = ['Age', 'Age - Group']
print(c) 
#compute eucledian distance between two series
k = pd.Series([10, 20, 30, 40, 50])
l = pd.Series([50, 60, 80, 90, 100])
m = np.linalg.norm(k - l)
print(m)