#Task 2
#  Write a Python program to calculate the area of a circle given its radius using the formula
#area=π×r^2 ( Take pi as 3.14)
import math
radius = float(input("Enter the radius \n"))
# area = pi radius**2
area = math.pi * (radius ** 2)
print(area)

# Create a program that takes two numbers as input and prints whether the first number is greater than, less than, or equal to the second number
num1 = int(input("Enter number 1: "))
num2 = int(input("Enter number 2: "))

result = "greater than" if num1 > num2 else "less than" if num1<num2 else "Equal to"
print(f"{num1} is {result} {num2}")

# = / == operator
# x = 10 # Assignment operator in python
a = 10
b = 15
result = (a == b)
print(result)
a = 15
b = 15
result = (a == b)
print(result)

# ** Operator
a1 = 2
b1 = 3
result = a1 ** b1
print(result)

# ^ (Bitwise XOR)opertor
x = 5  # Binary 0101
y = 2  # Binary  0011
result = x ^ y


