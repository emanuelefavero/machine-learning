import numpy as np

a = np.array(20)  # 0-D array, or scalar
b = np.array([1, 2])  # 1-D array, or vector
c = np.array([[1], [2]])  # 2-D array, or matrix
d = np.array([[[1], [2]], [[3], [4]]])  # 3-D array, or tensor

# Display the number of dimensions of each array
print(a.ndim)  # 0
print(b.ndim)  # 1
print(c.ndim)  # 2
print(d.ndim)  # 3

# Define the number of dimensions of the array
e = np.array([1, 2], ndmin=3)
print(e)  # [[[1 2]]]

# Get the data type of the array
print(type(a))  # <class 'numpy.ndarray'>

# TIP: ndarray means n-dimensional array
