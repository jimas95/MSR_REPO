cols = 4
rows = 4


def printMaze():
    fileName = "defaultMaze.txt"
    f = open(fileName, "r")
    maze = f.read()
    print(maze)

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





def readMaze():
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




