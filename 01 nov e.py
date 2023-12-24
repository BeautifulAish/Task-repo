numlist = [-10, 20, 25, 70, 100, 80]


def num_greater_10(num):
    return num > 10


List_of_numbers_greater_10 = list(filter(num_greater_10, numlist))
print(list_of_numbers_greater_10)

# by using lambda exp - lamda is used fpor simple exp 
numlist = [-10, 20, 25, 70, 100, 80]


#def num_greater_10(num):
 #   return num > 10

List_of_numbers_greater_10 = list(filter(lambda num: num>10, numlist))
print(list_of_numbers_greater_10)

