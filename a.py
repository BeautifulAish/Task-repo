#Define the list of numbers
numbers = [1, 2, 2, 4, 5, 3, 3, 6]

# Create a dictionary to count the occurrences of each number
count_dict = {}
non_duplicate_values = []

# Count occurrences of each number in the list
for num in numbers:
    if num in count_dict:
        count_dict[num] += 1
    else:
        count_dict[num] = 1

# Find non-duplicate values
for num in numbers:
    if count_dict[num] == 1:
        non_duplicate_values.append(num)

# Print non-duplicate values
print("duplicate values:", non_duplicate_values)