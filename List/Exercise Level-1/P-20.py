# To slice out the middle IT company or companies from the it_companies list, you need to determine the middle index or indices, 
# depending on whether the list has an odd or even length.
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
print("Before Slicing: ",it_companies)
# Determine the middle index or indices
length = len(it_companies)
middle_index = length // 2

# Slice out the middle IT company or companies
middle_companies = it_companies[middle_index] if length % 2 != 0 else it_companies[middle_index - 1:middle_index + 1]

# Print the result
print("Middle IT company or companies:", middle_companies)
