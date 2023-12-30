# You can change the name of one of the IT companies in the it_companies list to uppercase (excluding 'IBM') using the upper() method.
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
print ("Before Changing : ", it_companies)

# Change the name of one company to uppercase (excluding 'IBM')
company_to_change = 'Microsoft'  # Choose the company you want to change
if company_to_change != 'IBM':
    index_to_change = it_companies.index(company_to_change)
    it_companies[index_to_change] = company_to_change.upper()

# Print the updated list
print("Updated list of IT companies:", it_companies)
