class Myclass:
    name = None


def print_my_name(self):
    print("Your name is ->" + self.name)


Pramod_obj_ref = Myclass()
pramod_obj_ref.name = "Pramod"
pramod_obj_ref.print_my_name()
