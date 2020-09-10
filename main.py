import Maze
import MazeSolver
cols = 4
rows = 4

robotPos = (0,0)


if __name__ == "__main__":
    print ("Hello Mr. Robot")
    Maze.readMaze()
    Maze.printMaze()
    myMaze = Maze.getMaze()
    print (myMaze)
    MazeSolver.solveMaze(myMaze,(0,0),(4,4))



