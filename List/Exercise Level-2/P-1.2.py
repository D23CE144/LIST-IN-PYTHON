# Certainly! After finding the minimum and maximum age, you can add them back to the ages list using the append() method.
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

# Sort the list
ages.sort()

# Find the min and max age
min_age = min(ages)
max_age = max(ages)

# Add min and max age back to the list
ages.append(min_age)
ages.append(max_age)

# Print the updated list
print("Updated ages list:", ages)
# The ages list has the minimum and maximum ages appended to the end of the list.