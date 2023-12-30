# You can divide the countries list into two equal or nearly equal lists by using list slicing based on the length of the list.
countries = ['USA', 'Canada', 'India', 'China', 'Brazil', 'UK', 'Germany', 'France']

# Determine the middle index or indices
length = len(countries)
middle_index = length // 2

# Divide the countries list
if length % 2 != 0:
    first_half = countries[:middle_index + 1]
    second_half = countries[middle_index + 1:]
else:
    first_half = countries[:middle_index]
    second_half = countries[middle_index:]

# Print the result
print("Countries:", countries)
print("First half:", first_half)
print("Second half:", second_half)
