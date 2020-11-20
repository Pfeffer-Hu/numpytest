import numpy as np

array = np.array([[0,2,3],[0,2,3],[0,2,3]])
print(array)
print(array.shape)
isnan = ~np.isnan(array)

print(isnan)
#Test whether any array element along a given axis evaluates to True.
# np.array.any()是或操作，任意一个元素为True，输出为True。
print(isnan.any(axis=0))
print(isnan.any(axis=1))



