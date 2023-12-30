# To "destroy" or remove the it_companies list entirely from the program, you can use the del statement to delete the variable.
it_companies = ['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']
print("Before Removing: ",it_companies)
# Destroy the IT companies list
del it_companies

# Attempting to print the list will result in an error
try:
    print("Updated list of IT companies:", it_companies)
except NameError as e:
    print("Error:", e)
