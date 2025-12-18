"""
QUESTION:
Write a function `nextGeneration(grid)` that takes a 2D array `grid` of 0s and 1s as input and returns a new 2D array representing the next state of the cells based on the following rules:
- Any live cell with fewer than two live neighbors dies.
- Any live cell with two or three live neighbors lives on to the next generation.
- Any live cell with more than three live neighbors dies.
- Any dead cell with exactly three live neighbors becomes a live cell.
"""

def nextGeneration(grid):
    rows = len(grid)
    cols = len(grid[0])
    new_grid = [[0 for _ in range(cols)] for _ in range(rows)]

    for i in range(rows):
        for j in range(cols):
            live_neighbors = 0
            for x in range(max(0, i-1), min(rows, i+2)):
                for y in range(max(0, j-1), min(cols, j+2)):
                    if (x, y) != (i, j) and grid[x][y] == 1:
                        live_neighbors += 1

            if grid[i][j] == 1:
                if live_neighbors < 2 or live_neighbors > 3:
                    new_grid[i][j] = 0
                else:
                    new_grid[i][j] = 1
            else:
                if live_neighbors == 3:
                    new_grid[i][j] = 1

    return new_grid