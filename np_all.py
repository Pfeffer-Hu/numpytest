import numpy as np

a = np.array([[True,False],[True,True]])
# That means the AND operation has been done along x-axis
b = np.all(a,axis = 0)

print("a:\n", a)
print("b:\n", b)

print(b == None)

