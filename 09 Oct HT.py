# Create a program by taking 2 numbers from users,Add 1-2 duplicate print non duplicate numbers
numbers = [1, 2, 2, 4, 5, 3, 3, 6]
non_duplicates = []
for num in numbers:
    if numbers.count(num) == 1:
        non_duplicates.append(num)
        print("Non-duplicate elements:", non_duplicates)


