import numpy as np

# test 2 dimentional data
data =np.arange(800).reshape(100,8)

np.random.seed(10)
ratio = np.random.rand(100) < 0.8
new_data = data[ratio,...,4:6]
print(new_data)
