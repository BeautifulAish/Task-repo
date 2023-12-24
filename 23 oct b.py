# input = input("Enter the input string \n")
# palindrome checker by reverse slicing

original_str = "ISHITA"
rev_str = original_str[::-1]  # String slicing
print(rev_str)

if original_str == rev_str:
    print("It is palindrome")

else:
    print("It is not palindrome")


