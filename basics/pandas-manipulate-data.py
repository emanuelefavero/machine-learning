import pandas as pd

# A Pandas Series is a single column from a DataFrame
# (@see pandas-read-data.py)

# Select a single column
df = pd.read_csv("data/titanic.csv")
col = df["Age"]
print(col)
