import numpy as np
import pandas as pd # type: ignore
#create a series from list, dict & numpy array
x = pd.Series([1, 2, 3, 4, 5])
print(x)
x1 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
y1 = pd.Series(x1)
print(y1)
x2 = {'Afnaan': 38, 'Billu': 44, 'J leel': 62, 'Mamle': 54, 'kaala':58}
y2 = pd.Series(x2)
print(y2)
#convert the index of series into a column of DataFrame
k = pd.Series([10, 20, 30 ,40], index = ['a', 'b', 'c', 'd'])
print(k)
df = k.reset_index()
df.columns = ['Index', 'Value']
print(df)
#combine many series to form DataFrame
l = pd.Series(['Appul', 'Orange', 'Aalo'], name = 'Fruits & Veggies')
l1 = pd.Series(['Duktoor', 'Engineer aka jobless', 'Teachur'], name = 'Profession')
l2 = pd.Series(['Burgman', 'Dio', 'Civic'], name = 'Vehiculs')
df = pd.concat([l, l1, l2], axis = 1)
print(df)