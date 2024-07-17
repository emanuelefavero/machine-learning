import pandas as pd

# A DataFrame is a 2-dimensional labeled data structure
# with columns of potentially different types.

# Read CSV file from data folder
# TIP: The path is relative to the root folder where you run the script
df = pd.read_csv("data/titanic.csv")

# Show the first 5 rows
print(df.head())

# Display all columns
pd.options.display.max_columns = None

# Show statistics about the data (count, mean, std, min, 25%, 50%, 75%, max)
print(df.describe())
# NOTE: Only numeric columns are shown
