"""
QUESTION:
Write a function `numIslands` that takes a 2D grid of 0s and 1s as input and returns the number of islands. An island is a group of 1s connected horizontally or vertically. The function should modify the input grid.
"""

def numIslands(grid):
    def dfs(i, j):
        if i<0 or i>=len(grid) or j<0 or j>=len(grid[0]) or grid[i][j] != 1:
            return
        grid[i][j] = 0
        dfs(i-1, j)
        dfs(i+1, j)
        dfs(i, j-1)
        dfs(i, j+1)
  
    count = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 1:
                dfs(i, j)
                count += 1
    return count