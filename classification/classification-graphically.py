import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("data/titanic-big.csv")
plt.scatter(df["Fare"], df["Age"], c=df["Survived"])
plt.xlabel("Fare")
plt.ylabel("Age")
plt.title("Titanic passengers")

# TIP: Survived: yellow dots, did not survive: purple dots

# ----------------------------
# The task of a linear model is to find the line that
# best separates the two classes (survived and did not survive)

# EQUATION OF A LINE:
# 0 = ax + by + c
# where a, b, c are the coefficients of the line
# and x, y are the features (Fare, Age)
# TIP: ax means a multiplied by x
# To find out if a point is on the line, we can substitute the x and y values
# into the equation and see if the result is 0
# EXAMPLE: 0 = 2x + 3y - 5
# 2, 3 and 5 are the coefficients of the line
# If we substitute x=1 and y=1, we get 0 = 2*1 + 3*1 - 5 = 0,
# so (1, 1) is on the line
# TIP: If the value is positive, the point is above the line
# If the value is negative, the point is below the line

# ----------------------------
# LOGISTIC REGRESSION
# Is a way to find the line that best separates the two classes

# Add a line to the plot (hardcoded)
plt.plot([30, 100], [0, 80], color="magenta")
plt.legend(["Did not survive", "Prediction line"], loc="upper right")

# Show the plot
plt.show()
