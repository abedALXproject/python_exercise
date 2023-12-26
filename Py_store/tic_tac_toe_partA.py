# / /  0
#----- 1
# / /  2
#----- 3
# / /  4

def drowFild():
    for row in range(5):#0,1,2,3,4
        if row % 2 == 0:
            #print writting line
            for column in range(5):
                if column % 2 == 0:
                    if column != 4:
                        print(" ",end="")
                    else:
                        print(" ")
                else:
                    print("|",end="")
        else:
            print("-----")

player = 1
currentFild = [[" "," "," "],#element1
               [" "," "," "],#element2
               [" "," "," "],#element3
               ]
print(currentFild)
while(True):
    print("player turn: ",player)
    moverow = int(input("Enter the row: "))
    movecolumn = int(input("Enter the column: "))
    if player == 1:
        #make move for play1
        currentFild[movecolumn][moverow] = "x"
        player = 2
    else:
        #make move for pla2
        currentFild[movecolumn][moverow] = "o"
        player = 1
    print(currentFild)
