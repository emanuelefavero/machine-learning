import numpy as np

# Numpy Data Types

# i - integer
array = np.array([-1, 1])
print(array.dtype)  # int64

# b - boolean
array = np.array([True, False])
print(array.dtype)  # bool

# u - unsigned integer (positive integer)
# TIP: dtype is also used for setting the data type of the array
array = np.array([1, 2], dtype="uint64")
print(array.dtype)  # uint64

# f - float
array = np.array([1.2, 2.5])
print(array.dtype)  # float64

# c - complex (complex number)
array = np.array([1 + 2j, 3 + 4j])
print(array.dtype)  # complex128

# m - timedelta (time duration)
# TIP: np.timedelta64(1, "D") represents 1 day,
# np.timedelta64(4, "h") represents 4 hours
array = np.array([np.timedelta64(1, "D"), np.timedelta64(4, "h")])
print(array)  # [24 4]
print(array.dtype)  # timedelta64[h]
# TIP: You could also set the data type to "timedelta64[s]" for seconds etc...

# M - datetime (date and time)
array = np.array(["2024-07-17"], dtype="datetime64[D]")
print(array.dtype)  # datetime64[D]
print(array)  # ['2024-07-17T00']
# TIP: datetime64[Y] will only return the year etc...
