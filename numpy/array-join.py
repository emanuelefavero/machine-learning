import numpy as np

# * concatenate() METHOD
# Join two arrays
array1 = np.array([1, 2])
array2 = np.array([3, 4])
array = np.concatenate((array1, array2))
print(array)  # [1 2 3 4]

# Join two 2-D arrays along rows (axis=1)
array1 = np.array([[1, 2], [3, 4]])
array2 = np.array([[5, 6], [7, 8]])
array = np.concatenate((array1, array2), axis=1)
print(array)  # [[1 2 5 6] [3 4 7 8]]

# TIP: axis=1 means join along columns

# Join two 2-D arrays along columns (axis=0)
array1 = np.array([[1, 2], [3, 4]])
array2 = np.array([[5, 6], [7, 8]])
array = np.concatenate((array1, array2))  # axis=0 is the default
print(array)  # [[1 2] [3 4] [5 6] [7 8]]

# * stack() METHOD
# Join two arrays along a new axis using the stack() method
array1 = np.array([1, 2])
array2 = np.array([3, 4])
array = np.stack((array1, array2), axis=1)
print(array)  # [[1 3] [2 4]]

# ------------------------------
# HELPER FUNCTIONS

# * hstack() METHOD
# hstack() stacks arrays along rows
array1 = np.array([1, 2])
array2 = np.array([3, 4])
array = np.hstack((array1, array2))
print(array)

# TIP: hstack() is equivalent to concatenate() with axis=0

# * vstack() METHOD
# vstack() stacks arrays along columns
array1 = np.array([1, 2])
array2 = np.array([3, 4])
array = np.vstack((array1, array2))
print(array)  # [[1 2] [3 4]]

# TIP: vstack() is equivalent to concatenate() with axis=1

# * dstack() METHOD
# dstack() stacks arrays along height (depth)
array1 = np.array([1, 2])
array2 = np.array([3, 4])
array = np.dstack((array1, array2))
print(array)  # [[[1 3] [2 4]]]
