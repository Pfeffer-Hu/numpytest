import numpy as np

a = np.arange(16).reshape(4,4)
b = np.empty((4,4))

# a numpy is a iterable object
for i, ele in enumerate(a):
    b[i,0:b.shape[1]] = ele


print(b)

c = np.array([1])
print(np.append(c,2))

