"""
QUESTION:
Write a function `minPathSum(grid)` that calculates the minimal path sum from the top left to the bottom right of a given 2D grid. The path can only be constructed by moving right or down, and if a cell contains -1, it cannot be traversed. If there is no possible path, return -1; otherwise, return the minimal path sum.
"""

def minPathSum(grid):
    m = len(grid)
    n = len(grid[0])
    for i in range(1, n):
        if grid[0][i] != -1 and grid[0][i-1] != -1:
            grid[0][i] += grid[0][i-1]
        else:
            grid[0][i] = -1
    for i in range(1, m):
        if grid[i][0] != -1 and grid[i-1][0] != -1:
            grid[i][0] += grid[i-1][0]
        else:
            grid[i][0] = -1
    for i in range(1, m):
        for j in range(1, n):
            if grid[i][j] != -1:
                if grid[i-1][j] != -1 and grid[i][j-1] != -1:
                    grid[i][j] += min(grid[i-1][j], grid[i][j-1])
                elif grid[i-1][j] != -1:
                    grid[i][j] += grid[i-1][j]
                elif grid[i][j-1] != -1:
                    grid[i][j] += grid[i][j-1]
                else:
                    grid[i][j] = -1
    return -1 if grid[-1][-1] == -1 else grid[-1][-1]