cols = 4
rows = 4



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



