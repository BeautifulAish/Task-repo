# List
my_list = [1, 2, 3, 4]  # Int
my_list2 = [True, 1, "Ayush"]  # Dff data types

print("initial list: ", my_list)

print("Element of index :", my_list[2])

# Changing an element
my_list[3] = 25
print("List after changing element at index 3:", my_list)

# Append #Adding at end
my_list.append(7)
print("List of appending:", my_list)

# Extend ()
my_list.extend([8, 9])
print("list of extending:", my_list)

# Insert()
# my_list.insert (__index 1, __object'b')
print("List after inserting 'b' at index 1:", my_list)

# Remove
my_list.remove(9)
print("List after removing 9:", my_list)

# Copy
my_copy_list = my_list.copy()
print(my_copy_list)

#Clear
my_list.clear()
print("initial_list:", my_list)

print(my_copy_list)
#print("Index of '3'in the list:", my_list.index(3)) #After list cleared no index is present
print("Index of '3' in the list:", my_copy_list.index(3))

my_copy_list.sort()
my_copy_list.reverse()
my_copy_list

print(my_copy_list[0])
#Length
print(len(my_copy_list))

#Copy
my_list = my_copy_list.copy()
print(my_list.remove(3))     # Remove first occurrence of value
