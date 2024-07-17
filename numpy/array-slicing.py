import numpy as np

# TIP: In Python, the colon (:) is used to slice an array.
# The start index will be included, but the end index is not

array = np.array([1, 2, 3, 4, 5, 6, 7, 8])


# Slice the array from the beginning to the 4th element
print(array[:4])  # [1 2 3 4]

# Slice the array from the 4th element to the end
print(array[4:])  # [5 6 7 8]

# Negative slicing:
print(array[:-4])  # [1 2 3 4]

# Step
print(array[1:5:2])  # [2 4]

# Return every other element in the array
print(array[::2])  # [1 3 5 7]
print(array[1::2])  # [2 4 6 8]

# Slice 2-D array
array = np.array([[1, 2, 3], [4, 5, 6]])
print(array[1, 2:3])  # 6

# Return the first element of both arrays
print(array[0:2, 0])  # [1 4]
