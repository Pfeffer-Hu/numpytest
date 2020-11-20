import numpy as np

# 1 x 3 x 1 x 2
a = np.arange(6).reshape((1,3,1,2))
print(a)

# the postion of 0 and 1 don't matter.

b = np.swapaxes(a, 0, 1)

c = np.swapaxes(a, 1, 0)

print(c.shape)
print(c)

for ele in c:
    print(ele)