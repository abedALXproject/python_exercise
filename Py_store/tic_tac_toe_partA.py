# / /  0
#----- 1
# / /  2
#----- 3
# / /  4

def drowFild(field):
    for row in range(5):#0,1,2,3,4

        if row % 2 == 0:
            practicalrow = int(row/2)
            #print writting line
            for column in range(5):
                if column % 2 == 0:
                    practicalcolumn = int(column/2)
                    if column != 4:
                        print(field[practicalcolumn][practicalrow],end="")
                    else:
                        print(field[practicalcolumn][practicalrow])
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
drowFild(currentFild)
while(True):
    print("player turn: ",player)
    moverow = int(input("Enter the row: "))
    movecolumn = int(input("Enter the column: "))
    if player == 1:
        #make move for play1
        if currentFild[movecolumn][moverow] == " ":
            currentFild[movecolumn][moverow] = "x"
            player = 2
    else:
        #make move for pla2
        if currentFild[movecolumn][moverow] == " ":
            currentFild[movecolumn][moverow] = "o"
            player = 1
    drowFild(currentFild)

