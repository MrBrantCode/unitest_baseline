"""
QUESTION:
Implement a function `numIslands(grid)` that takes a 2D binary grid `grid` as input where '1' represents land and '0' represents water. The function should return the total number of distinct islands in the grid, where an island is defined as a contiguous landmass formed by horizontally or vertically adjacent land cells. The grid is surrounded by water and contains at least one cell. The dimensions of the grid are within the range 1 <= m, n <= 300, where m and n are the number of rows and columns in the grid, respectively.
"""

def numIslands(grid):
    def dfs(grid, i, j):
        if i<0 or j<0 or i>=len(grid) or j>=len(grid[0]) or grid[i][j] != '1':
            return 
        grid[i][j] = '0'
        dfs(grid, i+1, j)
        dfs(grid, i-1, j)
        dfs(grid, i, j+1)
        dfs(grid, i, j-1)
        
    if not grid:
        return 0
        
    count = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == '1':
                dfs(grid, i, j)
                count += 1
    return count