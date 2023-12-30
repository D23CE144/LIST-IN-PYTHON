# You can unpack the first three countries and the rest as Scandinavian countries using list unpacking in Python.
countries = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']

# Unpack the first three countries and the rest as Scandinavian countries
first_country, second_country, third_country, *scandic_countries = countries

# Print the result
print("First country:", first_country)
print("Second country:", second_country)
print("Third country:", third_country)
print("Scandinavian countries:", scandic_countries)
# the first three countries are unpacked into separate variables (first_country, second_country, and third_country), 
# and the rest are unpacked into the scandic_countries list using the * operator. 
# Adjust the variable names as needed for your specific use case.