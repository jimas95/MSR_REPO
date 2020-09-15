import numpy as np
import random

#0 if matrix is a wall, 1 if it is a free space

def getOneHopNeighbor(cellTuple, gridSize):
    neighbors = []
    if 0 <= cellTuple[0] - 1:
        neighbors.append((cellTuple[0] - 1, cellTuple[1]))
    if 0 <= cellTuple[1] - 1:
        neighbors.append((cellTuple[0], cellTuple[1] - 1))
    if cellTuple[1] + 1 < gridSize:
        neighbors.append((cellTuple[0], cellTuple[1] + 1))
    if cellTuple[0] + 1 < gridSize:
        neighbors.append((cellTuple[0] + 1, cellTuple[1]))
    return neighbors


if __name__ == "__main__":
    size = random.randint(3, 10)
    #size = 6
    #All cells are walls.
    maze = np.zeros((size, size))
    frontierList = []
    #Randomly choose a cell B and mark it as free.
    BRow = random.randint(0, size - 1)
    BCol = random.randint(0, size - 1)
    maze[BRow, BCol] = 1
    path = [(BRow, BCol)]
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
        Cneighbors = getOneHopNeighbor((CRow, CCol), size)
        sum = 0
        for i in range(len(Cneighbors)):
            sum += maze[Cneighbors[i]]
        if sum == 1:
            maze[CRow, CCol] = 1
            path.append((CRow, CCol))
            for t in Cneighbors:
                if maze[t] == 0:
                    frontierList.append(t)

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












