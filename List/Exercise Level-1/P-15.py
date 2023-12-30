# You can check if a certain company exists in the it_companies list using the in keyword. 

it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']

# Check if a certain company exists
company_to_check = 'Microsoft'
if company_to_check in it_companies:
    print(f"{company_to_check} exists in the list.")
else:
    print(f"{company_to_check} does not exist in the list.")
