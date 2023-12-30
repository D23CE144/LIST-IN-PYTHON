# To remove the first IT company from the it_companies list, you can use the pop() method or slice the list. 
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']

print("Before Removing: ",it_companies)
# Remove the first IT company using pop()
first_company_removed = it_companies.pop(0)

# Print the updated list and the removed company
print("Updated list of IT companies:", it_companies)
print("Removed company:", first_company_removed)
