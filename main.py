cols = 4
rows = 4

#type here....!
#thank you !
#Kailey: 
def printMaze(maze):
    print (maze)
    for col in range(cols):
        #for row in rows:
        print(" ____     ____    ____    ____")
        print()
        print(" |  |     |  |    |  |    |  |") 
        print(" ____     ____    ____    ____")

def readMaze():
    fileName = "defaultMaze.txt"
    f = open(fileName, "r")
    lines = f.readlines()
    for line in lines:
        #print("new line : " + line)
        temp=line.strip().split()
        # okei so now temp has all the values of the first row from the matrix 


if __name__ == "__main__":
    print ("Hello Mr. Robot")
    print("-----")
    f = open("defaultMaze.txt", "r")
    #print(f.read())
    realMaze = f.read()
    #printMaze(realMaze)
    readMaze()



