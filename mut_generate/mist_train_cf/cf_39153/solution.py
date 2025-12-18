"""
QUESTION:
Implement the function `grid_game(grid)` that takes a 2D array `grid` as input, where each element is either 0 (empty cell) or 1 (obstacle), and returns the maximum number of obstacles the player can avoid while navigating from the top-left to the bottom-right corner, moving only down or right at each step. The grid has at least one cell and at most 100 cells in each dimension.
"""

def grid_game(grid):
    rows, cols = len(grid), len(grid[0])
    
    max_obstacles = [[0] * cols for _ in range(rows)]
    
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                max_obstacles[i][j] = 0
            elif i == 0 and j == 0:
                max_obstacles[i][j] = 0
            elif i == 0:
                max_obstacles[i][j] = max_obstacles[i][j-1] + 1
            elif j == 0:
                max_obstacles[i][j] = max_obstacles[i-1][j] + 1
            else:
                max_obstacles[i][j] = max(max_obstacles[i-1][j], max_obstacles[i][j-1]) + 1
    
    return max_obstacles[rows-1][cols-1]