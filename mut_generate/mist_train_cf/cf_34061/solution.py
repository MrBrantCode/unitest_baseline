"""
QUESTION:
Implement a function `countInternalSectors(grid)` that takes a 2D grid of characters as input, where 'X' represents a filled cell and '.' represents an empty cell, and returns the total count of internal sectors. An internal sector is a contiguous area of the grid completely surrounded by filled cells.
"""

def countInternalSectors(grid):
    def is_internal_sector(i, j):
        if i <= 0 or j <= 0 or i >= len(grid) - 1 or j >= len(grid[0]) - 1:
            return False
        return grid[i-1][j] == 'X' and grid[i+1][j] == 'X' and grid[i][j-1] == 'X' and grid[i][j+1] == 'X'

    count = 0
    for i in range(1, len(grid) - 1):
        for j in range(1, len(grid[0]) - 1):
            if grid[i][j] == '.' and is_internal_sector(i, j):
                count += 1
    return count