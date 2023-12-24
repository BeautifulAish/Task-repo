# Task 1
# Python program to count vowel or consonant of the given string
st = input("Please enter a string as you wish: ")
vowels = 0
consonants = 0
for i in str:
    if (i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u' or
            i == 'A' or i == 'E' or i == 'I' or i == 'O' or i == 'U'):
        vowels = vowels + 1  # vowel counter is incremented by 1
    else:
        consonants = consonants + 1
# consonant counter is incremented by 1
print("The number of vowels:", vowels \n)
print("\nThe number of consonant:", consonants)

"""Task 2-✅ Right Triangle Star Pattern
*
**
***
****
*****"""

for i in range(6):
    print()
    for j in range(i):
        print("*", end="")

"""
✅ Create a Function with a Parameter which can do x^y
"""
x=int(input("Enter x value: "))
y=int(input("Enter y value: "))

def power(x,y):
    z=x**y
    return z

c=power(x,y)
print(c)

#✅ Create a Lambda expression to triple power 2**3 a number

LE=lambda x,y: x**3
print(LE(x,y))