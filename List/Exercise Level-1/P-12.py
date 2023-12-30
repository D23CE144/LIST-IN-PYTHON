it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
print ("Before Adding : ", it_companies)

# Insert a new IT company in the middle of the list
new_company = 'Wipro'
index_to_insert = len(it_companies) // 2
it_companies.insert(index_to_insert, new_company)

# Print the updated list
print("Updated list of IT companies:", it_companies)
