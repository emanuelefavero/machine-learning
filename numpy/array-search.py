import numpy as np

# Search arrays
# * where() METHOD
# Find the indices where the specified value is located
array = np.array([1, 2, 3, 4, 5, 4])
result = np.where(array == 4)
print(result)  # (array([3, 5]),)

# Print each index
for index in result[0]:
    print(index)  # 3 5

# Find indexes where the values are even
array = np.array([1, 2, 3, 4])
result = np.where(array % 2 == 0)
print(result)  # (array([1, 3]),)

# * searchsorted() METHOD
# Perform a binary search in the array (works only on sorted arrays)
array = np.array([1, 2, 3, 4, 5])
result = np.searchsorted(array, 3)
print(result)  # 2, index of 3

# Search from the right side
result = np.searchsorted(array, 3, side="right")
print(result)  # 3, index of 4
# ? Explanation: 3 is at index 2, but the right side of 3 is at index 3
