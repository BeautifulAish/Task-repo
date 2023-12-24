class Myclass:
    name = None
    last_name = None
    age = None


def print_my_name_with_last_name(self, last_name, age):
    print("Your name is -> " + self.name, last_name, age)


Pramod_obj_ref = Myclass()
pramod_obj_ref.name = "Pramod"
pramod_obj_ref.print_my_name_with_last_name(last_name "Dutta", age: 25)
