# Function
def Hello():
    print("I want to execute the code")


Hello()  # Call functionality

def funcwithparam(a):
    return a ** 2


# output = fuction
# with (i) param(2)
#   print(output)

# Palindrome checker
# 2 ways -  1. Traditional method 2. Builtin function
# user
input = input("Enter the input string /n")


# Palindrome - Reverse the string and match with old string, it should be same
# Using primitive loop
def reverse_str(input_str):
reverse_str = ""
for c in input_str:
    rev_str = c + reverse_str
    return_rev_str  # MADAM

original_str = "MADAM"
rev_str = reev_str(original_str)
print(rev_str)

if original_str == input_str:
    print("It is a palindrome")

else:
    ("It is not")
