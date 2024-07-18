import numpy as np

# Filter arrays
# In NumPy, you can filter an array using a boolean index list
# A boolean index list is a list of booleans corresponding to
# indexes in the array

# FILTER ELEMENTS LESS THAN 18
# Hardcoded filter:
array = np.array([14, 20, 16, 24])
filter_array = [True, False, True, False]
new_array = array[filter_array]
print(new_array)  # [14 16]

# Create filter array
filter_array = []
for element in array:
    if element < 18:
        filter_array.append(True)
    else:
        filter_array.append(False)
new_array = array[filter_array]
print(new_array)  # [14 16]

# * Directly filter the array (best way)
new_array = array[array < 18]
print(new_array)  # [14 16]

# Filter even numbers in the array
array = np.array([1, 2, 3, 4])
new_array = array[array % 2 == 0]
print(new_array)  # [2 4]

# Filter 2-D array (same as 1-D)
array = np.array([[1, 2], [3, 4]])
new_array = array[array % 2 == 0]
print(new_array)  # [2 4]
