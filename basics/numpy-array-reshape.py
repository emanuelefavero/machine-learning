import numpy as np

# * RESHAPE ARRAY
# The reshape() method changes the shape of the array

# Reshape 1-D array to 2-D array
array = np.array([1, 2, 3, 4])
reshaped = array.reshape(2, 2)
print(reshaped)  # [[1 2] [3 4]]

# Reshape 1-D array to 3-D array
array = np.array([1, 2, 3, 4, 5, 6, 7, 8])
reshaped = array.reshape(2, 2, 2)
print(reshaped)  # [[[1 2] [3 4]] [[5 6] [7 8]]]

# TIP: As long as the number of elements remains the same,
# you can reshape the array

# UNKNOWN DIMENSION
# You can pass -1 to the reshape method to let NumPy calculate
# the unknown dimension

# Reshape 2-D array to 1-D array
array = np.array([[1, 2], [3, 4]])
# reshaped = array.reshape(4)  # 4 elements
reshaped = array.reshape(-1)  # -1 means unknown dimension
print(reshaped)  # [1 2 3 4]

# ------------------------------

# TIP: Remember, to know the shape of the array,
# you can use the shape attribute
print(array.shape)  # (2, 2)
# TIP: To know the number of elements in the array,
# you can use the size attribute
print(array.size)  # 4

# ------------------------------

# FLATTEN ARRAY
# The flatten() method returns a 1-D array
array = np.array([[1, 2], [3, 4]])
flattened = array.flatten()
print(flattened)  # [1 2 3 4]

# RAVEL ARRAY
# The ravel() method returns a 1-D array
array = np.array([[1, 2], [3, 4]])
raveled = array.ravel()
print(raveled)  # [1 2 3 4]
print(raveled.base is array)  # True
# TIP: The ravel() method returns a view of the original array

# ------------------------------

# ROTATE ARRAY
# The rot90() method rotates the array by 90 degrees
array = np.array([[1, 2], [3, 4]])
rotated = np.rot90(array)
print(rotated)  # [[2 4] [1 3]]

# FLIP ARRAY
# The flip() method flips the array
array = np.array([[1, 2], [3, 4]])
flipped = np.flip(array)
print(flipped)  # [[4 3] [2 1]]

# FLIP ARRAY IN LEFT/RIGHT DIRECTION
array = np.array([[1, 2], [3, 4]])
flipped = np.fliplr(array)
print(flipped)  # [[2 1] [4 3]]

# FLIP ARRAY IN UP/DOWN DIRECTION
array = np.array([[1, 2], [3, 4]])
flipped = np.flipud(array)
print(flipped)  # [[3 4] [1 2]]
