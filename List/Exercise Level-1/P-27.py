front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node', 'Express', 'MongoDB']

# Join the lists
full_stack = front_end + back_end.copy()

# Insert 'Python' and 'SQL' after 'Redux'
insert_index = full_stack.index('Redux') + 1
full_stack[insert_index:insert_index] = ['Python', 'SQL']

# Print the result
print("Updated Full Stack:", full_stack)

# the copy() method is used to create a copy of the back_end list to avoid modifying the original list. 
# The index() method is then used to find the index of 'Redux', and the insert() method is used to insert 'Python' and 'SQL' after 'Redux'. 
# The result is stored in the full_stack variable.