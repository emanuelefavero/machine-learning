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

# STANDARD DEVIATION and VARIANCE
# Standard deviation - is the square root of the variance
# It measures how spread out the numbers are
# Variance - average of the squared differences from the mean

# Calculate the variance
distances_from_mean = []
for age in ages:
    distances_from_mean.append(abs(age - mean))
print(distances_from_mean)  # [8, 7, 5, 4, 1, 1, 6, 7, 11]

squared_distances = []
for distance in distances_from_mean:
    squared_distances.append(distance**2)  # or math.pow(distance, 2)
print(squared_distances)  # [64, 49, 25, 16, 1, 1, 36, 49, 121]

variance = sum(squared_distances) / len(ages)  # average of squared distances
print(round(variance, 2))  # 40.22

# Calculate the standard deviation
standard_deviation = variance**0.5  # or math.sqrt(variance)
print(round(standard_deviation, 2))  # 6.34, the square root of variance
