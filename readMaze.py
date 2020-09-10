cols = 4
rows = 4


def printMaze(maze):
    print (maze)
    for col in range(cols):
        #for row in rows:
        print(" ____     ____    ____    ____")
        print()
        print(" |  |     |  |    |  |    |  |") 
        print(" ____     ____    ____    ____")

def print_top_walls(line):
    text = ""
    for temp in line:
        cell = int(temp)
        if cell&1:
            text +="___"
        else:
            text+="   "
        text+="   "
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
    text =""

    for temp in line:
        cell = int(temp)
    text =""

    for temp in line:
        cell = int(temp)





def readMaze():
    fileName = "defaultMaze.txt"
    f = open(fileName, "r")
    lines = f.readlines()
    for line in lines:
        #print("new line : " + line)
        temp=line.strip().split()
        print_top_row(temp)


if __name__ == "__main__":
    print ("Hello Mr. Robot")
    print("-----")
    f = open("defaultMaze.txt", "r")
    #print(f.read())
    realMaze = f.read()
    #printMaze(realMaze)
    readMaze()



