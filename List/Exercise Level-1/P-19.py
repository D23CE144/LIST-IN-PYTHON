# To slice out the last three companies from the it_companies list, you can use negative indices. 
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']

print("Before Slicing: ",it_companies)
# Slice out the last 3 companies
last_three_companies = it_companies[-3:]

# Print the result
print("Last three companies:", last_three_companies)
