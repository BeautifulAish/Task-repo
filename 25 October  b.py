#my_list =[1,3,5,7,9,10]
# my_list = [True, "Arushi",15,20,30] - TypeError: '<' not supported between instances of 'str' and 'bool'
#my_list.sort()
#print(My_list)

squares = [1,4,5,10,20]
l = squares
l2=squares.copy() #l2 is shallow copy of list
squares [2] = 13
print(squares)
print(l)
print(l2)
print(id(l))
print(id(squares))
print(id(l2))