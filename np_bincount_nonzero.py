import numpy as np
"""
np.bincount: count the ele in array and be ordered 
np.nonzeros: return the indices of the elements that are non-zeros
"""
a = np.array([0,1,2,3,2,0,2,3,1,5])
b = np.bincount(a)
print(b)
print(np.nonzero(b))