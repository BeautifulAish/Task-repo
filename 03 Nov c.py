# car class
class Car:
    name = None
    color = None
    speed = None
    engine = None
    model_name = None

    # Self - is a special variable that is used within the context of OOPS
    # It's a reference to instance of class
    # Access and manipulate the attributes and methods of instance(object)/ helps to access attributes of it


def start_engine(self):
    print("starting an engine")


def drive(self):
    print("drive")


def brake(self):
    print("brake")


def who_is_driving(self):
    print("who is driving-->" + self.name)   #automative it will take tesla, lambo


tesla_obj_ref = Car()  # This is a instance of a Class - Object
lambo_obj_ref = Car()  # This is a instance of a Class - object

tesla_obj_ref.name = "Tesla"
lambo_obj_ref.name = "Lambo"

tesla_obj_ref.who_is_driving()
lambo_obj_ref.who_is_driving()


