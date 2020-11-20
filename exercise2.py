import numpy as np

a = np.arange(9).reshape(3,3)

b = np.add(a,3)

m = np.empty((0,3))

c = np.concatenate((a,b),axis = 0)
print(c)
d = np.concatenate((c,m),axis = 0)
print(d.astype(int))
