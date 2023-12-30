ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

# Sort the list
ages.sort()

# Find the median age
length = len(ages)
middle_index = length // 2

if length % 2 != 0:
    median_age = ages[middle_index]
else:
    median_age = (ages[middle_index - 1] + ages[middle_index]) / 2

# Print the result
print("Sorted ages:", ages)
print("Median age:", median_age)
# The sort() method is used to sort the ages list, 
# and then the median age is calculated based on whether the list has an odd or even length.