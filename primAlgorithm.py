import numpy as np
import random

#0 if matrix is a wall, 1 if it is a space
if __name__ == "__main__":
    size = random.randint(3, 10)
    #size = 4
    #All cells are walls.
    maze = np.zeros((size, size))
    frontierList = []
    #Randomly choose a cell B and mark it as free.
    BRow = random.randint(0, size - 1)
    BCol = random.randint(0, size - 1)
    maze[BRow, BCol] = 1
    print("B is " + str((BRow, BCol)))
    #Add that cell's neighbors to the wall list.
    if 0 <= BRow - 1:
        frontierList.append((BRow - 1, BCol))
    if 0 <= BCol - 1:
        frontierList.append((BRow, BCol - 1))
    if BRow + 1 < size:
        frontierList.append((BRow + 1, BCol))
    if BCol + 1 < size:
        frontierList.append((BRow, BCol + 1))
    print(frontierList)
    #While the frontier list is not empty:
    while len(frontierList) != 0:
        #Randomly choose a wall C from the wall list
        randomIndex = random.randint(0, len(frontierList) - 1)
        (CRow, CCol) = frontierList[randomIndex]
        print("C is " + str((CRow, CCol)))
        #The wall divides two cells, A and B.
        if BRow < CRow:
            ARow = CRow + 1
            ACol = CCol
        elif CRow < BRow:
            ARow = CRow - 1
            ACol = CCol
        elif BCol < CCol:
            ARow = CRow
            ACol = CCol + 1
        else:
            ARow = CRow
            ACol = CCol - 1
        print("A is " + str((ARow, ACol)))
        #If either A or B is a wall
        if maze[BRow, BCol] == 0 or (0 <= ARow and ARow < size and 0 <= ACol and ACol < size and maze[ARow, ACol] == 0):
            # Let D be whichever of A and B that is the wall
            if maze[BRow, BCol] == 0:
                DRow = BRow
                DCol = BCol
            else:
                DRow = ARow
                DCol = ACol
            print("D is " + str((DRow, DCol)))
            #Make C free
            maze[CRow, CCol] = 1
            #Make D free
            maze[DRow, DCol] = 1
            #Add the walls of D to the wall list
            if 0 <= DRow - 1 and maze[DRow - 1, DCol] == 0:
                frontierList.append((DRow - 1, DCol))
            if 0 <= DCol - 1 and maze[DRow, DCol - 1] == 0:
                frontierList.append((DRow, DCol - 1))
            if DCol + 1 < size and maze[DRow, DCol + 1] == 0:
                frontierList.append((DRow, DCol + 1))
            if DRow + 1 < size and maze[DRow + 1, DCol] == 0:
                frontierList.append((DRow + 1, DCol))
        #Remove C from the wall list
        p = frontierList.pop(randomIndex)
        print(frontierList)

    print(maze)
    convertedMaze = np.zeros((size, size))
    for i in range(0, len(convertedMaze)):
        for j in range(0, len(convertedMaze[0])):
            value = 0
            if maze[i, j] == 0:
                value = 15
            else:
                if j - 1 < 0 or maze[i, j - 1] == 0:
                    value += 8
                if j + 1 >= size or maze[i, j + 1] == 0:
                    value += 4
                if i + 1 >= size or maze[i + 1, j] == 0:
                    value += 2
                if i - 1 < 0 or maze[i - 1, j] == 0:
                    value += 1
            convertedMaze[i, j] = value
    print(convertedMaze)
    mat = np.matrix(convertedMaze)
    with open('primAlgorithmMaze.txt', 'wb') as f:
        for line in mat:
            np.savetxt(f, line, fmt='%2d')












