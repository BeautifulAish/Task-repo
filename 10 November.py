# POLYMORPHISM
# It allows obj of different classes to be treated as objects of common base class / super class
# 1 obj hv many forms
Class shape:
def area(self):
    print("Area of shape")

Class Rectangle(shape):

def __init__(self, length, width):
    self.length = length
    self.width = width


def area(self):
    return self.length * self.width


class Circle(shape):
    def __init__(self.radius):
    self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

    shape1 = Rectangle(length:3, width: 4):
    print(shape1.area())

    shape2 = Circle(12)
    print(shape2.area())


shape3 = shape()
print(shape3.area())
