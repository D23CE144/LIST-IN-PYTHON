# To compare the absolute differences between the minimum and average ages and the maximum and average ages using the abs() method.
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

# Calculate the average age
average_age = sum(ages) / len(ages)

# Calculate the differences
min_difference = abs(min(ages) - average_age)
max_difference = abs(max(ages) - average_age)

# Print the results
print("Ages:", ages)
print("Average age:", average_age)
print("Absolute difference (min - average):", min_difference)
print("Absolute difference (max - average):", max_difference)
# abs() is used to calculate the absolute differences between the minimum and average ages (abs(min(ages) - average_age)) 
# and the maximum and average ages (abs(max(ages) - average_age)). 
# This allows you to compare the magnitudes of these differences.