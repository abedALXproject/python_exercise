#I/O

#var = input("massage to my users")
"""
yourName = input("Enter your name: ")
print(yourName)
Age = input("Enter your Age: ")
print(int(Age) + 1)

#def function(input1,input2,input3):
    #Action
scores = []

for my in range(5):
    curScores = float(input("Enter your scores "+str(my+1)+": "))
    scores.append(curScores)
    print("The scores you have is:\n"+str(curScores))
print(scores)
"""

#file input and outout

#File = open("filename","r") #r+w+a
#File.close()

states = ["newyork", "calfornia", "london", "colombia", "chikago"]
statesTogo = open("statesplace.py","w")
for location in states:
    statesTogo.write(location + "\n")
statesTogo.close()

statesTogo = open("stateplace.py","r")

firstLine = statesTogo.readline()
print(firstLine)
for line in statesTogo:
    print(line, end = "")
#myfile = statesTogo.read()
#print(myFile)

statesTogo.close()

Makechange = "Nigeria"
statesTogo = open("statesplace.py","a")
statesTogo.write(Makechange)
statesTogo.close()

statesTogo = open("statesplace.py","r")
for line in statesTogo:
    print(line, end = "")
statesTogo.close()

for i in range(5):
    with open("statesplace.py"+str(i),"r") as statesTogo:
        for line in statesTogo:
            print(line)
