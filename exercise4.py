import numpy as np

a = np.arange(16).reshape(4,4)
b = np.empty((4,4))

## a numpy is a iterable object by row!
for i, ele in enumerate(a):
    b[i,0:b.shape[1]] = ele


print("b:\n",b)

c = np.array([1])
print(np.append(c,2))

##
"""
for example:
a = [[1,2,3],[1,2,3]] 
np.reshape(a,(,3)) error occurs!
np.reshape(a,(-1,3))  correct!


"""
d = np.reshape(b,(-1,4))
#f = np.reshape(b,(,4))  impossible
print(d)
print(d.shape)


print(np.array([1,2]).shape)

##
g = np.array([True,False,True,False])

print(b[g])

