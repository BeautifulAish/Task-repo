# Use the ternary operator to find the maximum of three numbers entered by the user.
num1 = float(input("Enter first number: "))
num2 = float(input("Enter Second number: "))
num3 = float(input("Enter third number: "))

max_number = num1 if ( num1 > num2 and num1 > num3) else (num2 if num2 > num3 else num3)
print("The maximum of {num1}, {num2} and {num3} is: {max_number}")

# square and cube of a given number
a= int(input("Enter value of a "\n))
square= (a**2)
cube=(a**3)
print("Square")
print("cube")
