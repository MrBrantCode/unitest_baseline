"""
QUESTION:
Write a function `count_connected_components(grid)` that takes a 2D grid represented as a list of binary numbers, where '1' represents an obstacle and '0' represents an empty space. The function should return the number of connected components in the grid, where connected components are groups of adjacent empty spaces (0-bits) connected horizontally or vertically.
"""

def count_connected_components(grid):
    def dfs(row, col):
        if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]) or grid[row][col] != '0':
            return
        grid[row] = grid[row][:col] + '1' + grid[row][col+1:]
        dfs(row+1, col)
        dfs(row-1, col)
        dfs(row, col+1)
        dfs(row, col-1)

    count = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == '0':
                dfs(i, j)
                count += 1
    return count