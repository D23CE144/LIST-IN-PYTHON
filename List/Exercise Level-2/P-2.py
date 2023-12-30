# To find the middle country or countries in a list, y
# you'll need to determine the middle index or indices based on whether the list has an odd or even length.
countries = ['USA', 'Canada', 'India', 'China', 'Brazil', 'UK', 'Germany', 'France']

# Determine the middle index or indices
length = len(countries)
middle_index = length // 2

# Find the middle country or countries
if length % 2 != 0:
    middle_country = countries[middle_index]
else:
    middle_country = countries[middle_index - 1:middle_index + 1]

# Print the result
print("Countries:", countries)
print("Middle country or countries:", middle_country)
