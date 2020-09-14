#reads maze from txt file
#file name defaultMaze.txt
cols = 4
rows = 4


def readMaze():
    fileName = "defaultMaze.txt"
    f = open(fileName, "r")
    maze = f.read()
    print(maze)

def getMaze():
    fileName = "defaultMaze.txt"
    f = open(fileName, "r")
    maze =[]
    while True:
        line = f.readline()
        if not line: 
            break
        rowList = []
        temp=line.strip().split()
        for item in temp:
            rowList.append(int(item))
        maze.append(rowList)
    return maze


def print_top_walls(line): 
    text = " "
    for temp in line:
        cell = int(temp)

        if cell&1:
            text +="____"
        else:
            text+="    "
    print(text)

def print_bottom_walls(line):
    text = ""
    for temp in line:
        cell = int(temp)
        if cell&2:
            text +="___"
        else:
            text+="   "
        text+="   "
    print(text)


def print_side_walls(line):
    text = ""
    for temp in line:
        cell = int(temp)
        if cell&8:
            text +="|"
        else:
            text+=" "

        text+="   "
    text+="|"
    print(text)





def printMaze():
    fileName = "defaultMaze.txt"
    f = open(fileName, "r")
    while True:
        line = f.readline()
        if not line: 
            break
        temp=line.strip().split()
        print_top_walls(temp)
        print_side_walls(temp)
        
        #print_bottom_walls(temp)
    print(" ________________")

