# Exception - abnormal event during execution, can be handled
# Error - specific code  --> 1gb - stack over flow
# 10, 12 error - difficult to overcome
# Memory error - Error - Restart, retry

a = int(input("Enter A number \n"))
b = int(input("Enter B number \n"))
try:
     c = a/b
     print(c)
except Exception as error:
     print("You are driving the value of A with zero. Please don't do it", error)