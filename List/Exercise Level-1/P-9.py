#You can print the first, middle, and last company from the it_companies list using index notation.

it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']

# Print the first, middle, and last companies
print("First company:", it_companies[0])
print("Middle company:", it_companies[len(it_companies) // 2])
print("Last company:", it_companies[-1])

#This assumes that the list has an odd length for the middle company to be well-defined. 
# If the list has an even length, you may need to adjust the logic accordingly.