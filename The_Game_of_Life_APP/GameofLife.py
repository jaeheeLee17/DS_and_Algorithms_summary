import sys
sys.path.append("H:\DS_and_Algorithms_summary\The_Game_of_Life_APP\Life_Grid_ADT")

# Program for playing the game of Life.
from life import LifeGrid

# Define the initial configuration of live cells.
# INIT_CONFIG = [(1, 2), (2, 1), (2, 2), (2, 3)]

# Set the size of the grid.
# GRID_WIDTH = 5
# GRID_HEIGHT = 5

# Indicate the number of generations.
# NUM_GENS = 8

def main():
    # Construct the game grid and configure it.
    print("Welcome to the game of life!")
    print("Enter the grid size: ", end=' ')
    GRID_SIZE = int(input())
    GRID_WIDTH, GRID_HEIGHT = GRID_SIZE, GRID_SIZE
    print("Enter the number of generation: ", end=' ')
    NUM_GENS = int(input())
    INIT_CONFIG = LifeGrid.RandomGridConfigure(GRID_WIDTH, GRID_HEIGHT)
    grid = LifeGrid(GRID_WIDTH, GRID_HEIGHT)
    grid.configure(INIT_CONFIG)

    # Play the game.
    print("Initial Configuration")
    draw(grid)
    for i in range(NUM_GENS):
        print("{} generations".format(i + 1))
        evolve(grid)
        draw(grid)

# Generates the next generation of organisms.
def evolve(grid):
    # List for storing the live cells of the next generation.
    liveCells = list()

    # Iterate over the elements of the grid.
    for i in range(grid.numRows()):
        for j in range(grid.numCols()):
            # Determine the number of live neighbors for this cell.
            neighbors = grid.numLiveNeighbors(i, j)

            # Add the (i, j) tuple to liveCells if this cell contains
            # a live organism in te next generation.
            if (neighbors == 2 and grid.isLiveCell(i, j)) or \
               (neighbors == 3):
               liveCells.append((i, j))

    # Reconfigure the grid using the liveCells coord list.
    grid.configure(liveCells)

# Prints a text-based representation of the game grid.
def draw(grid):
    for r in range(grid.numRows()):
        for c in range(grid.numCols()):
            if grid.isLiveCell(r, c):
                print('@', end=' ')
            else:
                print('.', end=' ')
        print('\n')

# Executes the main routine.
main()
