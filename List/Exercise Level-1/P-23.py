# To remove the last IT company from the it_companies list, you can use slicing
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']

print("Before Removing: ",it_companies)
# Remove the last IT company using slicing
it_companies = it_companies[:-1]

# Print the updated list
print("Updated list of IT companies:", it_companies)
