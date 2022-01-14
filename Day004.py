#Day004
#Random and python list

row1 = [' ',' ',' ']
row2 = [' ',' ',' ']
row3 = [' ',' ',' ']
map=[row1,row2,row3]
print(f"{row1} \n{row2} \n{row3}")
position = input("Where do you want to put the treasure?(Remeber X then Y eg. 31) \n")


if int(position[0]) == 1:
    if int(position[1]) == 1:
        row1[0] = 'X'
    elif int(position[1]) == 2:
         row1[1] = 'X'
    elif int(position[1]) == 3:
         row1[2] = 'X'
    else:
        print("Error on second digit")

elif int(position[0]) == 2:
    if int(position[1]) == 1:
        row2[0] = 'X'
    elif int(position[1]) == 2:
        row2[1] = 'X'
    elif int(position[1]) == 3:
        row2[2] = 'X'
    else:
        print("Error on second digit")

elif int(position[0]) == 3:
    if int(position[1]) == 1:
        row3[0] = 'X'
    elif int(position[1]) == 2:
         row3[1] = 'X'
    elif int(position[1]) == 3:
         row3[2] = 'X'
    else:
        print("Error on second digit")   
else:           
    print("Error on first digit")
print(f"{row1} \n{row2} \n{row3}")
