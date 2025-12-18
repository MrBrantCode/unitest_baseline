"""
QUESTION:
Implement the `jouer()` function to simulate the game of Jouer for a given number of generations and grid configuration. The function takes a 2D list `grid` where each cell is either 0 (dead) or 1 (alive) and an integer `generations` representing the number of generations to simulate. Return the final grid configuration after simulating the specified number of generations. 

The game's progression rules are as follows: 
1. Any live cell with fewer than two live neighbors dies.
2. Any live cell with two or three live neighbors lives on to the next generation.
3. Any live cell with more than three live neighbors dies.
4. Any dead cell with exactly three live neighbors becomes a live cell.
"""

def jouer(grid, generations):
    rows = len(grid)
    cols = len(grid[0])

    def count_live_neighbors(row, col):
        count = 0
        for i in range(max(0, row-1), min(rows, row+2)):
            for j in range(max(0, col-1), min(cols, col+2)):
                count += grid[i][j]
        count -= grid[row][col]
        return count

    def next_generation():
        new_grid = [[0] * cols for _ in range(rows)]
        for i in range(rows):
            for j in range(cols):
                live_neighbors = count_live_neighbors(i, j)
                if grid[i][j] == 1:
                    if live_neighbors < 2 or live_neighbors > 3:
                        new_grid[i][j] = 0
                    else:
                        new_grid[i][j] = 1
                else:
                    if live_neighbors == 3:
                        new_grid[i][j] = 1
        return new_grid

    for _ in range(generations):
        grid = next_generation()

    return grid