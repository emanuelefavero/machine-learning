import numpy as np

# * ITERATE ARRAY

# Iterate 1-D array
array = np.array([1, 2, 3])
for num in array:
    print(num)  # 1 2 3

# Iterate 2-D array
array = np.array([[1, 2], [3, 4]])
for row in array:
    for num in row:
        print(num)  # 1 2 3 4

# Iterate 3-D array
array = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
for matrix in array:
    for row in matrix:
        for num in row:
            print(num)  # 1 2 3 4 5 6 7 8

# Iterate 4-D array
array = np.array([[[[1], [2]], [[3], [4]]], [[[5], [6]], [[7], [8]]]])
for tensor in array:
    for matrix in tensor:
        for row in matrix:
            for num in row:
                print(num)  # 1 2 3 4 5 6 7 8


# Iterate array no matter the number of dimensions
def print_elements(array):
    for element in array:
        if isinstance(element, np.ndarray):
            print_elements(element)
        else:
            print(element)


# ------------------------------

# * NDITER METHOD
# You can use the nditer() method to iterate through the array
# no matter the number of dimensions
array = np.array([1, 2, 3])
for num in np.nditer(array):
    print(num)  # 1 2 3

array = np.array([[1, 2], [3, 4]])
for num in np.nditer(array):
    print(num)  # 1 2 3 4

# ITERATE ARRAY WITH DIFFERENT DATA TYPES
array = np.array([1, 2, 3])
for num in np.nditer(array, flags=["buffered"], op_dtypes=["S"]):
    print(num)

# TIP: The op_dtypes parameter is used to change
# the data type of the array elements
# TIP: The buffered flag is needed for memory purposes

# ITERATE ARRAY WITH DIFFERENT STEP SIZE
array = np.array([[1, 2], [3, 4]])
for num in np.nditer(array[:, ::2]):
    print(num)  # 1 3

# SHOW THE INDEX OF THE ELEMENT
array = np.array([1, 2, 3])
for index, num in np.ndenumerate(array):
    print(index, num)  # (0,) 1 (1,) 2 (2,) 3
