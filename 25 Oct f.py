#Sq of number using map function
numbers = [2, 3, 4, 5, 6]
sq_numbers = list(map(lambda x: x*x,numbers)) # Apply for  list,set,tuple
print(sq_numbers)

def triple(a):
    return a*3
sq_numbers = list(map(triple(), numbers))

