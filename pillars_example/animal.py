# create a class called Animal - file name with a - class name starts with A
# add the common attribute/variables behaviour/functions
# syntax class name: - class Animal:
class Animal: # Follow the correct naming convention and nest practices
    # We need to initialise the class with builtin method called __init__(self)
    # self refers to current class
    def __init__(self): # any attributes attached to the class should be part of init method
        self.alive = True
        self.spine = True
        self.eyes = True

    # let's create some methods to add common behaviours
    def breathe(self):
        return "keep breathing to stay alive"

    def eat(self):
        return "Time to eat!...."

    # create an object of this class


cat = Animal()  # This will create an object of our animal class
# print(cat.breathe())  # calling a method using object of the Animal class
# print(cat.eat())





