# Write a Python program to find the largest number in a l
def find_largest_number(numbers):
    if not numbers:
        return None  # Return None for an empty list

    largest = numbers[0]  # Assume the first number is the largest

    for number in numbers:
        if number > largest:
            largest = number

    return largest

# Example usage:
my_list = [12, 45, 74, 23, 98, 54, 32]
largest_number = find_largest_number(my_list)

if largest_number is not None:
    print(f"The largest number in the list is {largest_number}")
else:
    print("The list is empty.")


    # 2. Write a Python program to find the smallest number in a list.

List1 = [0,1,4,55,66,77,70,3]
List1.sort()
print(List1)
small = List1[0]
print(f'Smallest number in the list is {small}')
max = List1[len(List1)-1]
print(f'Max number in the list {max}')

#Write a Python program to sum all numbers in a list.
List1 = [8,21,30,4,3,50,10]
def sum_of_list(n):
    Sum = 0
    for i in n:
        Sum = Sum+i
    print("Sum of the list is", Sum)
sum_of_list(List1)
