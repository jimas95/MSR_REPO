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
    #lines = f.readlines()
    #print(lines)
    while True:
        line = f.readline()
        if not line: 
            break
        temp=line.strip().split()
        print_top_walls(temp)
        print_side_walls(temp)
        
        #print_bottom_walls(temp)
    print(" ________________")

if __name__ == "__main__":
    print ("Hello Mr. Robot")
    readMaze()
    print()



