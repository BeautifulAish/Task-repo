list = []  # To check list is empty/not
if not list:
    print("Empty")
else:
    print("not empty")

# POP
a = [1, 2, 3, 4, 5]
# Index =[0, 1, 2, 3, 4]
print(a.pop(1))  # Pop will remove index value # Remove and return item at index (default last).
print(a)
print(a.remove(4))  # Remove will ewmove the value not index # Remove doesn't return anything so result will be None
print(a)

print(type(12))  # Int
print(type("12"))  # Str
b = "15"
b1 = int(b)
b2 = 10.30
b3 = int(b2)
print(type(b))  # Str
print(type(b1))  # Int
print(type(b2))  # Float
print(type(b3))  # Int

t = True  # True is = 1, False = 0
print(int(t))

st = "pramod"
my_list = list(st)
print(my_list)
my_list.sort()
print(my_list)
