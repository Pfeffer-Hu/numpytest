import numpy as np
"""
a[a[:,1] == 3,:]:
if the 1st column is equal to 3, we can get the corresponding row

"""
a = np.arange(9).astype(int).reshape(3,3)
print(a[a[:,0] == 3,:])

a = np.arange(9).astype(int).reshape(3,3)
print(a)
print(a[:,0])

b = np.arange(3)
print(b)
c = np.hstack((a[:,0],b))
print(c)
