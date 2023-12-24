# Write a Python program to multiply all numbers in a list.
list=[2,4,7,10,12]
mult=1
for i in list:
 mult= mult*i
print("The multiplication of number is ",mult)

#Write a Python program to count the number of strings in a list where the string length is 2 or more
list2 = ["aa","ABC","Ind","AG","123","8","MOM"]
str=""
count=0
for i in list2:
    if type(i)==type(str) and len(i)>=2 and i[0]==i[-1]:
        count=count+1
        # print("yes")
    # else:
        # print("not")

print("Total strings : ",count)