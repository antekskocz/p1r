import numpy as np


class Grid:
    grid = []
    allowed = [[[i for i in range(1,10)] for x in range(9)] for y in range(9)]

    def __init__(self, grid):
        self.grid = grid

    def solve(self):
        return self.grid

    def print(self):
        for x in range(9):
            for y in range(9):
                print(self.grid[x][y],end =" ")
                if (y+1)%3 == 0:
                    print(" ",end="")
            if (x+1)%3 == 0:
                print()
            print()
        print()

def readGrid():
    rawGrid = ("003020600 900305001 001806400 "
               "008102900 700000008 006708200 "
               "002609500 800203009 005010300 ")
    numberGrid = [[int(ch) for ch in row] for row in rawGrid.split(" ")]

    return Grid(numberGrid)


def __main__():
    grid = readGrid()

    grid.print()
    grid.solve()
    grid.print()


__main__()
