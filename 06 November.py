# Constructor

Class Car:

name = "None"  # Class Variable

def __init__(self):
    print("I will be called first -->" + self.name)

def start_engine(self):
    peint("starting a Car")

Car1 = Car()
Car2 = Car()

printid(Car1)
printid(Car2)

# When Object is created special  function is called automatically __init__()
# For all the attribute you can initialize - Add some initial value
