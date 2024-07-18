import numpy as np

# Sort arrays

# TIP: The sort() method returns a copy of the array, leaving og array unchanged

array = np.array([3, 1, 2])
result = np.sort(array)
print(result)  # [1 2 3]

# Sort a 2-D array
array = np.array([[2, 3], [4, 1]])
result = np.sort(array)
print(result)  # [[2 3] [1 4]]

# Sort the array in descending order
array = np.array([3, 1, 2])
result = np.sort(array)[::-1]
print(result)  # [3 2 1]

# Sort array of other types
array = np.array(["banana", "apple"])
result = np.sort(array)
print(result)  # ['apple' 'banana']
