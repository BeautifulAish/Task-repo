# Conditions set of rules
age = float(input("Enter your age"))
print(age)

if age > 18:
    print("you are allowed to watch movie")
else:
    print("Yes")

x = 10
y = 20

if x > y:
    print("x is greater than y")
elif x < y:
    print("x is less than y")
else:
    print("x and y are equal")

#maximum of 3 numbers
a = float(input("Enter number first number: "))
b = float(input("Enter number second number: "))
c = float(input("Enter number third number: "))

max = None
if a>b and a>c:
    max = a
elif b>a and b>c:
    max = b
else:
    max = c
print(max)