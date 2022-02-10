# Python Inheritance
# in this tutorial I will cover inheritance
# in oop we are parent and child class
class Person: # this is the parent class
    def __init__(self, name, lastname, age):
        self.name = name.capitalize()
        self.lastname = lastname.capitalize()
        self.age = age
    def detail(self):
        print('wa wa wa')
    def skin_color(slef, colors):
        return colors
    def display_details(self):
        print(self.name, self.lastname, self.age)
        self.detail()
        print(self.skin_color('White'))
p = Person('saboor', 'samedi', 28)
p.display_details()



