# this code finds the solution of the maze
#Recursive Backtracking




# if (x,y outside maze) return false
# if (x,y is goal) return true
# if (x,y not open) return false
# mark x,y as part of solution path
# if (FIND-PATH(North of x,y) == true) return true
# if (FIND-PATH(East of x,y) == true) return true
# if (FIND-PATH(South of x,y) == true) return true
# if (FIND-PATH(West of x,y) == true) return true
# unmark x,y as part of solution path
# return false

maxCoord = 0
goalPos = (0,0)
maze = []
path = []


#return if we are allowed to go to this direction dir = 1,2,4,8
# dir = 1 is North since 0b1 = N
# dir = 2 is South since 0b10 = S
# dir = 4 is East since 0b100 = E
# dir = 8 is West since 0b1000 = W
#pos(x,y)
def canIgo(pos,dir):
    global maze
        # print ("can I go fuction :  position--> " +str(pos[0])+" " +str(pos[1]))
    cell = maze[pos[1]][pos[0]]
    if cell&dir: return False
    return True



#Check if we reach the goal
def reachGoal(pos):
    global goalPos,path
    if pos == goalPos:
        print("good job!")
        path[pos[1]][pos[0]] = True
        return True
    return False

def insideMaze(pos):
    if pos[0]> maxCoord: return False
    if pos[1]> maxCoord: return False
    if pos[0] < 0: return False
    if pos[1] < 0: return False
    return True

def find_path(pos):
    global path
    x = pos[0]
    y = pos[1]
    if (not insideMaze(pos))  : return False
    if reachGoal(pos)   : return True
    if path[y][x]==True : return False

    path[y][x] = True 
    pos=(x,y-1) 
    if(insideMaze(pos) and canIgo((x,y),1)): #1 is N
        if(find_path(pos) == True): return True # use canIgo first
    pos=(x+1,y)
    if(insideMaze(pos) and canIgo((x,y),4)):#4 is S
        if(find_path(pos) == True): return True
    pos=(x,y+1)
    if(insideMaze(pos) and canIgo((x,y),2)):#2 is S
        if(find_path(pos) == True): return True
    pos=(x-1,y)
    if(insideMaze(pos) and canIgo((x,y),8)):#8 is W
        if(find_path(pos) == True): return True

    path[y][x] = False
    return False




def solveMaze(mazeInput,StartPos,EndPos):
    global maze,path,maxCoord,goalPos

    maze = mazeInput
    maxCoord = len(maze)-1
    goalPos = EndPos
    print("goal position : " + str(goalPos[0]) + " " + str(goalPos[1]))
    # path = [[False]*mazeInput]*mazeInput
    print("path finding starts...")
    path = [[False,False,False,False],[False,False,False,False],[False,False,False,False],[False,False,False,False]]
    find_path(StartPos)
    print("Final path:")
    for i in range(len(path)):
        print(path[i])
