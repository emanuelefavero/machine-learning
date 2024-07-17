import pandas as pd

df = pd.read_csv("data/titanic.csv")

# TIP: You can use the .values attribute to get the values as a NumPy array

# Get values from a single column
print("Single column:")
print(df[["Fare"]].values)

# Get values from multiple columns
print("Multiple columns:")
print(df[["Fare", "Age"]].values)

# Get all values from the DataFrame
print("All values:")
print(df.values)

# Print all values from the DataFrame
# print("All values with Numpy:")
# for row in df.values:
#     for value in row:
#         print(value)

# NUMPY SHAPE ATTRIBUTE
# Get how many rows and columns are in our data
print("Shape:")
array = df[["Fare", "Age"]].values
print(array.shape)  # (4, 2) -> 4 rows, 2 columns
