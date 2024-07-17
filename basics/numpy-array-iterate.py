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
