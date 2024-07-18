import numpy as np

# * array_split() METHOD
# Split an array into multiple sub-arrays
array = np.array([1, 2, 3, 4])
new_array = np.array_split(array, 2)  # 2 is the number of sub-arrays
print(new_array)  # [array([1, 2]) array([3, 4])]

# Assign the sub-arrays to variables
[array1, array2] = new_array
print(array1)  # [1 2]
print(array2)  # [3 4]

# TIP: There is also the split() method but it will not adjust the elements
# when the array cannot be split evenly

# Split a 2-D array into multiple sub-arrays
array = np.array([[1, 2], [3, 4]])
new_array = np.array_split(array, 2)
print(new_array)  # [array([[1, 2]]) array([[3, 4]])]

# * hsplit() METHOD
# Split an array along the horizontal axis
array = np.array([[1, 2], [3, 4]])
new_array = np.hsplit(array, 2)
print(new_array)  # [array([[1], [3]]) array([[2], [4]])]

# TIP: There are also vsplit() and dsplit() methods for
# splitting along the vertical and depth axes
