

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import random

# Press the green button in the gutter to run the script.
Length = random.randint(1,10)
Width = random.randint(1,10)
print(Length)
print(Width)
Table = []
IslandBorderTable = []
for i in range(0,Width):
    LineTable = []
    BlankTable = []
    for v in range(0, Length):
        LineTable.append( random.randint(0, 1))
        BlankTable.append("")
    Table.append(LineTable)
    IslandBorderTable.append(BlankTable)

for item in Table:
    print(item)
def Check(y,x):

    if  0<= y-1 :
        if Table[y-1][x] == 1 and IslandBorderTable[y-1][x]!=1 :
            IslandBorderTable[y - 1][x] = 1
            Check(y-1,x)
    if  0<= x-1 :
        if Table[y][x-1] == 1 and IslandBorderTable[y][x-1]!=1 :
            IslandBorderTable[y][x-1] = 1
            Check(y, x-1 )
    if  y+1 <= Width-1:
        if Table[y+1][x] == 1  and IslandBorderTable[y+1][x]!=1:
            IslandBorderTable[y+1][x] = 1
            Check(y+1,x)
    if x+1 <= Length-1:
        if Table[y][x+1] == 1 and IslandBorderTable[y][x+1]!=1:
             IslandBorderTable[y][x+1] = 1
             Check(y,x+1)

for i in range(0,Length):

    if Table[0][i] == 1:
        IslandBorderTable[0][i] = 1
        Check(0,i)
for i in range(0,Length):

    if Table[Width-1][i] == 1:
        IslandBorderTable[Width-1][i] = 1
        Check(Width-1,i)
for i in range(0,Width):

    if Table[i][0] == 1:
        IslandBorderTable[i][0] = 1
        Check(i,0)
for i in range(0, Width):

    if Table[i][Length-1] == 1:
        IslandBorderTable[i][Length-1] = 1
        Check(i, Length-1)

for i in range(0,Width):
    for v in range(0, Length):
        if Table[i][v]==1 and (i!= 0 and i!= (Width-1)) and (v!= 0 and v!= (Length-1)) and IslandBorderTable[i][v]!= 1:
            Table[i][v]=0

print("\n")
for item in Table:
    print(item)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
