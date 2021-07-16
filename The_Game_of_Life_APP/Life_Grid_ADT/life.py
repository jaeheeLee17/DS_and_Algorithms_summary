import sys
sys.path.append("H:\DS_and_Algorithms_summary\Array_ADT")

# Implements the LifeGrid ADT for use with the game of life.
from array_structure import Array2D

class LifeGrid:
    # Defines constants to represent the cell states.
    DEAD_CELL = 0
    LIVE_CELL = 1

    # Creates the game grid and initializes the cells to dead.
    def __init__(self, numRows, numCols):
        # Allocate the 2-D array for the grid.
        self._grid = Array2D(numRows, numCols)
        # Clear the grid and set all cells to dead.
        self.configure(list())

    # Returns the number of rows in the grid.
    def numRows(self):
        return self._grid.numRows()

    # Returns the number of columns in the grid.
    def numCols(self):
        return self._grid.numCols()

    # configures the grid to contain the given live cells.
    def configure(self, coordList):
        # Clear the game grid.
        for i in range(self.numRows()):
            for j in range(self.numCols()):
                self.clearCell(i, j)

        # Set the indicated cells to be alive.
        for coord in coordList:
            self.setCell(coord[0], coord[1])

    # Does the indicated cell contain a live organism?
    def isLiveCell(self, row, col):
        if row >= 0 and row < self.numRows() and \
           col >= 0 and col < self.numCols():
           return self._grid[row, col] == LifeGrid.LIVE_CELL

    # Clears the indicated cell by setting it to dead.
    def clearCell(self, row, col):
        self._grid[row, col] = LifeGrid.DEAD_CELL

    # Sets the indicated cell to be alive.
    def setCell(self, row, col):
        self._grid[row, col] = LifeGrid.LIVE_CELL

    # Returns the number of live neighbors for the given cell.
    def numLiveNeighbors(self, row, col):
        nLiveNeighbors = 0
        for r in range(row - 1, row + 2):
            for c in range(col - 1, col + 2):
                if r == row and c == col:
                    continue
                if self.isLiveCell(r, c):
                    nLiveNeighbors += 1
        return nLiveNeighbors

    @staticmethod
    # Random Configuring initial grid
    def RandomGridConfigure(numRows, numCols):
        import random
        initial_liveCells = list()
        round = random.randint(1, max(numRows * numCols, 1))
        for i in range(round):
            row = random.randint(0, numRows - 1)
            col = random.randint(0, numCols - 1)
            initial_liveCells.append((row, col))
        return initial_liveCells
