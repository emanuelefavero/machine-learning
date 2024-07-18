import matplotlib.pyplot as plt
import pandas as pd

# A scatter plot is used to show all the values from your data on a graph
# In order to get a visual representation of our data,
# we have to limit our data to two features.

df = pd.read_csv("data/titanic.csv")

# Create a scatter plot and choose the colors of the dots
plt.scatter(df["Age"], df["Fare"], c="#f0f")

# Create a scatter plot with colored dots based on the "Pclass" column
# TIP: The "Pclass" column has 3 unique values (1, 2, 3),
# those will be represented by different colors
# plt.scatter(df["Age"], df["Fare"], c=df["Pclass"])  # ! UNCOMMENT TO SEE

# Label the axes
plt.xlabel("Age")
plt.ylabel("Fare")

# Title
plt.title("Titanic passengers")

# Line
# first two values are the x-axis, the last two are the y-axis
plt.plot([22, 38], [7, 71], color="#78ff78bf")

# Grid
plt.grid(True)

# Text
plt.text(22, 7, "Youngest", fontsize=10, color="blue")
plt.text(38, 71, "Oldest", fontsize=10, color="blue")

# Legend
plt.legend(["Passengers", "Line"])

# Show the plot
plt.show()
