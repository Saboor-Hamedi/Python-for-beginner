import random
# we start with classes and objects
#Python is an object oriented programming language.
#A Class is like an object constructor, or a "blueprint" for creating objects.
#to create class we must use keyword, "class"
class Dog:
    # pass, if your class is empty add keywor pass, to avoid getting error
    # every class has a pre-built function called, __init()__, 
    # if you're from java, this a constrcut, anytime you make a class, this function will be classed
    def __init__(self, name, age):
        self.name = name
        self.age = age 
        # self is used to access variables that belongs to the class
        # its not necessary to be self, you can write anything, the point is , the first paramter is object of the class
    def random_number(self, value):
        x_value = random.randint(0, value)
        print(f'Your random number is: {x_value}')
dog = Dog('Tomi', 0.6) # we create the object of our class
print(dog.name)
print(dog.age)
dog.random_number(10)



