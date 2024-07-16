import pandas as pd

df = pd.read_csv("data/titanic.csv")

# SELECTING

# Define a NumPy array with values from multiple columns
arr = df[["Pclass", "Fare", "Age"]].values
print("NumPy array:")
print(arr)

# Select a single element from a numpy array
print("Single element:")
print(arr[0, 1])  # 7.25, first row, second column

# Select a single row
print("Single row:")
print(arr[0])  # [3. 7.25 22]

# Select a single column
print("Single column:")
print(arr[:, 1])  # [ 7.25 71.2833  7.925 53.1 ...]

# MASKING
# Create a mask to filter values
# TIP: A mask is a boolean array that can be used to filter values

# Select all rows where Age is less than 30
mask = arr[:, 2] < 30
print("Mask:")
print(mask)  # [ True False  True ...]
print("Filtered values:")
print(arr[mask])  # Show only rows where Age is less than 30
# TIP: We can also use the mask directly in the array `arr[arr[:, 2] < 30]`

# Select all rows where Pclass is equal to 1, show only the Age column
arr = df[["Pclass", "Age"]].values
first_class_passengers = arr[arr[:, 0] == 1]
first_class_passengers_ages = first_class_passengers[:, 1]
print("First class passengers ages:")
print(first_class_passengers_ages)  # [38 35 ...]

# SUMMING AND COUNTING
# Summing an array of boolean values will count the number of True values,
# giving us for instance the count of passengers in first class:

arr = df[["Pclass", "Age"]].values
mask = arr[:, 0] == 1  # select items where column 0 (Pclass) is equal to 1
print("First class passengers count:")
print(mask)  # [ False True False ...]
print(mask.sum())  # 2 passengers in first class
