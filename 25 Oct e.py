list = [1, 2, 3, 4, 5]
print(dir(list))  # We will get all functions
# ['append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']

# MAP and Filter

sq = lambda x: x * x
result = sq(5)
print(result)

# Map # We will apply fun for each item and apply functions
numbers = [2, 3, 4, 5, 6]
sq_numbers = []
for i in numbers:
    # append object to the end of the list. """
    sq_numbers.append(sq(i))

print(sq_numbers)
sq_numbers2 = [2, 3, 4, 5, 6]


