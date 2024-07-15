# AVERAGES
# Mean - average of all numbers
# Add all numbers and divide by the number of numbers

ages = [15, 16, 18, 19, 22, 24, 29, 30, 34]
mean = round(sum(ages) / len(ages))
print(mean)  # 23

# Median - middle number of a sorted list
# If the list has an even number of elements,
# the median is the average of the two middle numbers
middle = int(len(ages) / 2)
if len(ages) % 2 == 0:
    median = (ages[middle - 1] + ages[middle]) / 2
else:
    median = ages[middle]
print(median)  # 22
# TIP: You can also use the floor division operator (//) to get the middle index
# middle = len(ages) // 2

# PERCENTILES
# 25th percentile - 25% of the data is below this value
percentile_25 = ages[int(len(ages) * 0.25)]  # or / 4
print(percentile_25)  # 18

# 75th percentile - 75% of the data is below this value
percentile_75 = ages[int(len(ages) * 0.75)]  # or / 1.33
print(percentile_75)  # 29
