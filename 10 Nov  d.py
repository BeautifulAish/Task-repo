# Method Overloading
# Python will not support Method Overloading in traditional method
# Same name of a fun with diff parameter

ClassMathUtil:


# def add(Self, a, b)
def add(Self, a, b=0, c=0)
    # def add(self, a, b, c):
    return a + b + c

Math = MathUtil()
# math.add(a:1 b:2)
Op0 = math.add(1)
Op1 = math.add(a:1, b: 2)
Op2 = math.add(a:1, b: 2, c: 3)
print(Op1)
print(Op2)
# math.add(1,2,3) - Python will not support Method Overloading in traditional method

# it is possible when we use diff param
