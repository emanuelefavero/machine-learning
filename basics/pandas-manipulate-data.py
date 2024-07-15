import pandas as pd

# A Pandas Series is a single column from a DataFrame
# (@see pandas-read-data.py)

# Select a single column
df = pd.read_csv("data/titanic.csv")
col = df["Age"]
print(col)

print("\n --- \n")  # separator

# Select multiple columns
cols = df[["Age", "Fare"]]
print(cols.head())

# TIP: .head() is used to show only the first 5 rows
