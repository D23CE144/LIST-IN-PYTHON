# You can access the first item, the middle item, and the last item of a list in Python using index notation. 
my_list = [1, 2, 3, 'four', 5.0, True, 'six', 7, 'eight', 9.99]

# Get the first item
first_item = my_list[0]

# Get the middle item (assuming the list has an odd length)
middle_item = my_list[len(my_list) // 2]

# Get the last item
last_item = my_list[-1]

# Print the results
print("First item:", first_item)
print("Middle item:", middle_item)
print("Last item:", last_item)

# Keep in mind that the calculation for the middle item (len(my_list) // 2) assumes that the list has an odd length. 
# If the list has an even length and you want the exact middle, you might need to adjust the logic accordingly.