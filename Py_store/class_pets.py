# This is a class pets practice

class Pets:
    def __init__(self,n,a,h,p):
        self.Name = n
        self.age = a
        self.hunger = h
        self.Playful = p

# getters
    def getName(self):
        return self.Name

    def getAge(self):
        return self.age

    def getHunger(self):
        return self.hunger

    def getPlayful(self):
        return self.Playful

    # setters

    def setName(self,name):
        self.Xname = name

    def setAge(self,Age):
        self.age = Age

    def setHunger(self,hunger):
        self.hunger

    def setPlayful(self,Playful):
        self.Playful = Playful

    def __str__(self):
        return (self.Name + " is " + str(self.age) + " years old")
class Human:
    def __init__(self,Name,Pets):
        self.myName = Name
        self.myPets = Pets

    def hasPets(self):
        if len(self.myPets) != 0:
            return "yes"
        else:
            return "No"

# pets1 = Pets("kamisi",3,False,True)

# print(pets1.getName())
# print(pets1.getPlayful())
# pets1.setName("cleta")
# print(pets1.getName())
# print(pets1.Name)

# pets1.Name = "inno"
# print(pets1.Name)

class Dog(Pets):
    def __init__(self,Name,age,hunger,Playful,bread,favtoy):
        Pets.__init__(self,Name,age,hunger,Playful)
        self.bread = bread
        self.favorightoy = favtoy
    def WanToPlay(self):
        if self.Playful == True:
            return ("Dogs want to play with: "+ self.favorightoy)
        else:
            return ("Dog dosn't want to play")
class Cat(Pets):
    def __init__(self,Name, age,hunger,Playful,place):
        Pets.__init__(self,Name,age,hunger,Playful)
        self.FavoritePlaceToSit = place

    def WanToSit(self):
        if self.Playful == False:
            print("the cat wan to sit in:",self.FavoritePlaceToSit)
        else:
            print("the cat wan to play")
    def __str__(self):
        return (self.Name + " like to sit in " + self.FavoritePlaceToSit)

myCat = Cat("ketrin",5,False,True,"sheds")
myCat.WanToSit()
print(myCat)

myDog = Dog("kyara",5,False,True,"boy","stick")
Play = myDog.WanToPlay()
print(Play)

myDog.Playful = False

Play = myDog.WanToPlay()
print(Play)
print(Dog)

HumanLook = Human("cleta",[myDog,myCat])
hasPetss = HumanLook.hasPets()
print(hasPetss)

print(HumanLook.myPets[0].Name)
