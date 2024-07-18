import matplotlib.pyplot as plt
import pandas as pd

# A scatter plot is used to show all the values from your data on a graph
# In order to get a visual representation of our data,
# we have to limit our data to two features.

df = pd.read_csv("data/titanic.csv")

# Create a scatter plot
plt.scatter(df["Age"], df["Fare"])

# Create a scatter plot with colored dots
# TIP: The "Pclass" column has 3 unique values (1, 2, 3),
# those will be represented by different colors
# plt.scatter(df["Age"], df["Fare"], c=df["Pclass"])  # ! UNCOMMENT TO SEE

# Label the axes
plt.xlabel("Age")
plt.ylabel("Fare")

# Add a title
plt.title("Titanic passengers")


# Show the plot
plt.show()
