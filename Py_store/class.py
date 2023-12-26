"""
class livingston:
    pass
inoo = livingston()
age = livingston()
inoo.name = "eyemouse"
age.year = "4"
inoo.secondname = "manass"
print(inoo.name, age.year, inoo.secondname)

class detail:
    def __init__(self, my_name, ages, address, phone):
        self.name = my_name
        self.age = ages
        self.address = address
        self.num = phone
my_detail = detail("cleta abednego", "31", "masaka", "09088765543")
print(my_detail.name, my_detail.age, my_detail.address, my_detail.num)
"""

class Person:

    # init method or constructor
    def __init__(self, name):
        self.name = name

    # Sample Method
    def say_hi(self):
        print('Hello, my name is', self.name)


# Creating different objects
p1 = Person('Nikhil')
p2 = Person('Abhinav')
p3 = Person('Anshul')

p1.say_hi()
p2.say_hi()
p3.say_hi()
