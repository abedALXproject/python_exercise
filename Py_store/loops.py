members = ["joe", "mike", "inno", "boi", "longs"]

post = 0

for me in members:
    if me == "inno":
        print(me)
        break
    post += 1
print(post)
print(members)

index = 0
for current in range(len(members)):
    if members[current] == "boi":
        print("Have break",index)
        break
    print("Not Break",index)
print(current+1)

for num in range(10):
    if num % 3 == 0:
        print(num)
        print("Divisible by 3")
        continue
    print(num)
    print("Not Divisible by 3")

length = 10
myPrint = "A"
for post in range(1,length+1):
    print(myPrint*post)
    
    
for post in range(length-1,0,-1):
    print(myPrint*post)

