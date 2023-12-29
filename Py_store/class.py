# this is a general class practies
"""
class livingston:
    pass
inoo = livingston()
age = livingston()
inoo.name = "eyemouse"
age.year = "4"
inoo.secondname = "manass"
print(inoo.name, age.year, inoo.secondname)
"""



"""
class detail:
    def __init__(self, my_name, ages, address, phone):
        self.name = my_name
        self.age = ages
        self.address = address
        self.num = phone
my_detail = detail("cleta abednego", "31", "masaka", "09088765543")
print(my_detail.name, my_detail.age, my_detail.address, my_detail.num)
"""

"""
class Person:

     init method or constructor
    def __init__(self, name):
        self.name = name

     Sample Method
    def say_hi(self):
        print('Hello, my name is', self.name)


Creating different objects
p1 = Person('Nikhil')
p2 = Person('Abhinav')
p3 = Person('Anshul')

p1.say_hi()
p2.say_hi()
p3.say_hi()
"""
# class member:
#    def __init__(self):
#       self.Attribute = 0
#
#    def AnotherFunction(self):
#       Action(s)
"""
class Team:

    def __init__(self, name = "name", origin = "oringin"):
        self.teamName = name
        self.Teamorigin = origin

    def DefineTeamName(self, name):
        self.TeamName = name

    def DefineTeamNameOrigin(self,origin):
        self.TeamOrigin = origin


Team1 = Team("john", "london")
Team2 = Team("dave", "canada")
Team3 = Team()

print(Team3.teamName, Team3.Teamorigin)
print(Team2.teamName, Team2.Teamorigin)
print(Team1.teamName, Team1.Teamorigin)

Team1.DefineTeamName("cleta")
print(Team1.TeamName)
Team1.DefineTeamNameOrigin("jos")
print(Team1.TeamOrigin)
"""
# class inheritance

class Team:

    def __init__(self, name = "name", origin = "oringin"):
        self.TeamName = name
        self.TeamOrigin = origin

    def DefineTeamName(self, name):
        self.TeamName = name

    def DefineTeamNameOrigin(self,origin):
        self.TeamOrigin = origin

# class InheritanceClassName(parentClass):
#    def __init__(self, Input1, Input2):
#        parentclass.__init__(self)
#        self.Attribute1 = Input1
#        self.Attribute2 = Input2
#        self.Attribute3 = 0
#
#    def AnotherMethod(self):
#        Action(s)


class Player(Team):
    def __init__(self,PlayerName,Point,TeamName,TeamOrigin):
        Team.__init__(self,TeamName,TeamOrigin)
        self.PlayerName = PlayerName
        self.PlayerPoint = Point

    def ScorePoint(self):
        self.PlayerPoint += 1

    def SetName(self,Name):
        self.PlayerName = Name

    def __str__(self):
        return self.PlayerName + " has score: " + str(self.PlayerPoint) + " Point"

Player1 = Player("sid",0,"messi","canada")

print(Player1.PlayerName)
print(Player1.PlayerPoint)

# Player1.DefineTeamName("messi")

print(Player1.TeamName)
print(Player1.TeamOrigin)

Player1.ScorePoint()
print(Player1.PlayerPoint)

Player1.SetName("Lee")

print(Player1.PlayerName)
print(Player1)
