# Membership operator
my_list = [15,10,56,30]
print(10 in my_list) #True / False - Bool
print(11 in my_list)
print(11 not  in my_list)

#Identity Operator
#Checks value used with list, returns true if both variables are in same object
# It returns False not returns True if both variables are not the same object
x = [1,2,3]
y = [1,2,3]
print(x is y)

a = 15
b = 15
print(a is b)
print(id(a))
print(id(b))
print(a is not b)