# To remove the middle IT company or companies from the it_companies list, 
# you need to determine the middle index or indices and then use the pop() method or slicing.
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
print("Before Removing: ",it_companies)

# Determine the middle index or indices
length = len(it_companies)
middle_index = length // 2

# Remove the middle IT company or companies
if length % 2 != 0:
    middle_company_removed = it_companies.pop(middle_index)
else:
    middle_companies_removed = it_companies[middle_index - 1:middle_index + 1]
    del it_companies[middle_index - 1:middle_index + 1]

# Print the updated list and the removed company or companies
print("Updated list of IT companies:", it_companies)
print("Removed company or companies:", middle_company_removed if length % 2 != 0 else middle_companies_removed)
