


class Person():
  def __init__(self, name, age):
    self.name = name
    self.age = age
 
  def display(self):
    print(self.name, self.age)
 
# child class
class Student(Person):
  def __init__(self, name, age):
    self.sName = name
    self.sAge = age
    # inheriting the properties of parent class
    super().__init__("Rahul", age)
 
  def displayInfo(self):
    print(self.sName, self.sAge)
 
obj = Student("Mayank", 23)
obj.display()
obj.displayInfo()

# My_family
class family(object):
    def __init__(self, first, second, exception, last):
        self.Alpha = first
        self.Tongret = second
        self.exception = exception
        self.Joice = last

    @property
    def Apha(self):
        self.__Alpha

    @Alpha.setter
    def Alpha(self, age):
        self.__age = 43

    @property
    def Tongret(self):
        self.__Tongret

    @Tongret.setter
    def Tongret(self, age):
        self.__Tongret = 39

    @property
    def exception(self):
        self.__exception

    @exception.setter
    def exception(self, X):
        self.__X = inheritance

    @property
    def Joice(self):
        self.__Joice

    @Joice.setter
    def Joice(self):
        self.__Joice = 23

    #def __str__(self):
     #   return "first is {} and sec is {} and except {} and last is {}".format(type(self).__name__, self.Aplha, self.Tongret, self.exception, self.Joice)

my_family = family()
print(my_family.Alpha, myfamily.Tongret, my_family.exception, my_family.Joice)
"""
