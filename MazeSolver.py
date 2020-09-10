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
makredMaze = []
N = 1
S = 2
E = 4
W = 8


#return if we are allowed to go to this direction dir = 1,2,4,8
# dir = 1 is North since 0b1 = N
# dir = 2 is South since 0b10 = S
# dir = 4 is East since 0b100 = E
# dir = 8 is West since 0b1000 = W
#pos(x,y)
def canIgo(pos,dir):
    global maze

    cell = maze[pos[1]][pos[0]]
    print (cell)
    if cell&dir: return False
    return True



#Check if we reach the goal
def reachGoal(pos):
    global goalPos
    if pos == goalPos:
        print("good job!")
        return True
    return False

def insideMaze(pos):
    if pos[0]> maxCoord: return False
    if pos[1]> maxCoord: return False
    if pos[0] < 0: return False
    if pos[1] < 0: return False
    return True

def find_path(pos):
    global makredMaze
    x = pos[0]
    y = pos[1]
    if insideMaze(pos) : return False
    if reachGoal(pos): return True
    if makredMaze[y][x] : False
    makredMaze[y][x] = True
    if(find_path((x,y-1)) == True): return True # use canIgo first
    if(find_path((x+1,y)) == True): return True
    if(find_path((x,y+1)) == True): return True
    if(find_path((x-1,y)) == True): return True
    makredMaze[y][x] = False
    return False
# if (x,y not open) return false
# mark x,y as part of solution path
# if (FIND-PATH(North of x,y) == true) return true
# if (FIND-PATH(East of x,y) == true) return true
# if (FIND-PATH(South of x,y) == true) return true
# if (FIND-PATH(West of x,y) == true) return true

# unmark x,y as part of solution path
# return false



def solveMaze(mazeInput,StartPos,EndPos):
    global maze,maxCoord,goalPos

    maze = mazeInput
    maxCoord = len(maze)-1
    goalPos = EndPos
    # robotPos = StartPos
    # print(canIgo((0,1),1))
    # print(canIgo((0,1),2))
    # print(canIgo((0,1),4))
    # print(canIgo((0,1),8))
