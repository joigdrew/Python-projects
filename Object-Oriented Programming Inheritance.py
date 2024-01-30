#-----------------------------------------------------------------------
#-----------------------------------------------------------------------


#Code not working perfectly yet, raising an error.
"""
Traceback (most recent call last):
  File "C:location of file\"name of file", line 39, in <module>
    d.set_breed(breed)
TypeError: Dog.set_breed() takes 1 positional argument but 2 were given
"""

class Animal():
    category = "None"
    def __init__(self):
        pass

    def move(self):
        print("")

class Dog(Animal):  #The Dog class inherits from the Animal class. This is what this means, placing it in the bracket, like the arguement or the parent class.
    def __init__(self):
        self.category = "Dog"

    breed = None

    def set_breed(self):
        self.breed = breed

    def get_category(self):
        return self.category

    def get_breed(self):
        return self.breed

breed = input("Animl Breed: ")

d = Dog()

d.set_breed(breed)

print("Category: ", d.get_category())
print("Breed: ", d.get_breed())