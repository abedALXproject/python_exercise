#data structure
#set data structure
"""
Sets = {"elmt1", "Elmt2", "Elmt1", "Elmt4"}
print(Sets)
if "me" in Sets:
    print("cleta")
elif "Elmt4":
    print("python is wowowow")
else:
    print("rong input")
    
    
myList = []
for me in range(5):
    List = input("enter you list: ")
    myList.append(List)

listSet = set(myList)
print(myList)
print(listSet)
if "nigeria" in listSet:
    print("atended")
    """
    
#Dictionary = {"key1": "key2": "key3": "key5": "key6"}
"""
myList = []
for me in range(5):
    List = input("enter you list: ")
    myList.append(List)
    
myDictionary = {}
for clist in myList:
    if clist in myDictionary:
        myDictionary[clist] += 1
    else:
        myDictionary[clist] = 1
print(myDictionary)
"""

blackShoesDic = {24:2,56:5,32:4,54:1,11:0}
print(blackShoesDic)
while(True):
    buySize = int(input("What is you shoe size you want to buy?\n"))
    if buySize < 0:
        break
    if blackShoesDic[buySize] > 0:
        blackShoesDic[buySize] -= 1
    else:
        print("shoes size is not in the store")
    print(blackShoesDic)
