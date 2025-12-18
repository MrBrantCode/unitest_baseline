"""
QUESTION:
Write a function `surroundedOpenSpaces(grid: str) -> int` that takes a string representing a 2D grid of 'X' and 'O' characters as input, where 'X' represents obstacles and 'O' represents open spaces, and the grid is surrounded by '}' characters on all sides. The function should return the number of open spaces ('O') that are completely surrounded by obstacles ('X') in the grid, considering an open space is completely surrounded if all its adjacent cells (up, down, left, and right) are obstacles.
"""

def entance(grid: str) -> int:
    rows, cols = len(grid), len(grid[0])
    count = 0
    for i in range(1, rows - 1):
        for j in range(1, cols - 1):
            if grid[i][j] == 'O':
                if (grid[i-1][j] == 'X' or i == 0) and (grid[i+1][j] == 'X' or i == rows-1) and (grid[i][j-1] == 'X' or j == 0) and (grid[i][j+1] == 'X' or j == cols-1):
                    count += 1
    return count