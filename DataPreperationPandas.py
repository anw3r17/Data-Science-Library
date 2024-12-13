import numpy as np
import pandas as pd # type: ignore
#normalize all columns in a DataFrame
x = pd.DataFrame({'column 1': [1, 2, 3, 4, 5],
               'column 2': [6, 7, 8, 9, 10]})
print(x)
mini = np.min(x)
maxi = np.max(x)
xnormie = (x - mini) / (maxi - mini)
print(xnormie)
#compute correlation of each row with the succeding row
x1 = pd.DataFrame({'a': [1, 2, 3, 4, 5],
                   'b': [2, 4, 6, 8, 10],
                   'c': [3, 6 , 9, 12, 15]})
corr = x1.corrwith(x1.shift(-1))
print(corr)
#compute autocorrelations of a numeric series
n = pd.Series(np.random.randint(1, 100, 100))
auto = n.autocorr()
print(auto)

                  