
#a program that take an input of attendance name and there country and there age
#and save the attendance in a file
"""
attendanceNumber = 2
attendanceData = []

registerdAttend = 0
storeFile = open("attendanceData.txt", "w")

while (registerdAttend < attendanceNumber):
    tmp_data = []
    name = input("Please enter your name: ")
    tmp_data.append(name)
    country = input("Please enter your country of origin: ")
    tmp_data.append(country)
    age = int(input("Please enter your age: "))
    tmp_data.append(age)
    print(tmp_data)
    attendanceData.append(tmp_data)
    print(attendanceData)
    registerdAttend += 1

for attendance in attendanceData:
    for data in attendance:
        storeFile.write(str(data))
        storeFile.write(" ")
    storeFile.write("\n")
storeFile.close()
"""

inputFile = open("attendanceData.txt", "r")
inputList = []
for line in inputFile:
    tmp_attend = line.strip().split()
    print(tmp_attend)
    inputList.append(tmp_attend)
    print(inputList)

Age = {}
for part in inputList:
    tmp_age = int(part[-1])
    if tmp_age in Age:
        Age[tmp_age] += 1
    else:
        Age[tmp_age] = 1
print(Age)

Countries = {}
for part in inputList:
    tmp_country = part[-2] # or 1
    if tmp_country in Countries:
        Countries[tmp_country] += 1
    else:
        Countries[tmp_country] = 1
print("countries that attend:",Countries)
oldest = 0
youngest = 100
mostOccurenAge = 0
counter = 0

for tempage in Age:
    if tempage > oldest:
        oldest = tempage
    if tempage < youngest:
        youngest = tempage
    if Age[tempage] >= counter:
        counter = Age[tempage]
        mostOccuringAge = tempage
print(oldest)
print(youngest)
print("most occuring age is:",mostOccuringAge,"with",counter,"attend")
inputFile.close()
