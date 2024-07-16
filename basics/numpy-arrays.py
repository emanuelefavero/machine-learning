import pandas as pd

df = pd.read_csv("data/titanic.csv")

# Define a NumPy array with values from multiple columns
arr = df[["Pclass", "Fare", "Age"]].values
print("NumPy array:")
print(arr)

# Select a single element from a numpy array
print("Single element:")
print(arr[0, 1])  # 7.25, first row, second column

# Select a single row
print("Single row:")
print(arr[0])  # [3. 7.25 22.]

# Select a single column
print("Single column:")
print(arr[:, 1])  # [ 7.25 71.2833  7.925 53.1 ...]
