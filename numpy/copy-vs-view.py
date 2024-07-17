import numpy as np

# * COPY VS VIEW
# Copy: The copy owns the data and any changes made to the copy
# will not affect the original array and vice versa
array = np.array([1, 2])
copy = array.copy()
copy[0] = 3

print(array)  # [1 2]
print(copy)  # [3 2]

# View: The view does not own the data and any changes made to the view
# will affect the original array
array = np.array([1, 2])
view = array.view()
view[0] = 3

print(array)  # [3 2]
print(view)  # [3 2]

# CHECK IF THE ARRAY OWNS THE DATA:
# We can use the base attribute to check if the array owns the data
# If the array owns the data, the base attribute will return None
print(copy.base)  # None
print(view.base)  # [3 2]

print(copy.base is None)  # True, copy owns the data
print(view.base is None)  # False, view does not own the data

# TIP: Owning the data means that
# the array is the only one that has access to the data
