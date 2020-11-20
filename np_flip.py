import numpy as np
"""
Reverse the order of elements in an array along the given axis.

The shape of the array is preserved, but the elements are reordered.
"""

A = np.arange(4).reshape((2,2))
print(A)

print(np.max(np.flip(A),axis = 0))
a = np.max(np.flip(A),axis = 0)
print(np.flip(a))
print(np.flip(A, 0))
print(np.flip(A, 1))
