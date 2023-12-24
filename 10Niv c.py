# Method Overriding - Same name in parent and child or
# Child override parent fun
# Super means call my parent
class Animal:
def sound(self):
    print("Animal Sound")


Class_Dog(Animal)
def sound(self):
    super().sound() # by using super dog can cll sound from parent
    print("Dog sound")


animal = Animal()
animal.sound()

dog = Dog()
dog.sound()
