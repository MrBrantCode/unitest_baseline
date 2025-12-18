"""
QUESTION:
Implement a function `canReachEnd(maze: List[List[str]]) -> bool` that determines whether the bottom-right corner of a given maze can be reached from the top-left corner. The maze is represented as a 2D grid, where each cell is either a wall ('#') or an empty space ('.'). The player can move either down or right at each step, but cannot move through walls.
"""

from typing import List

def canReachEnd(maze: List[List[str]]) -> bool:
    rows, cols = len(maze), len(maze[0])
    dp = [[False] * cols for _ in range(rows)]
    
    dp[0][0] = True  # Starting point is reachable
    
    # Fill in the first row
    for col in range(1, cols):
        if maze[0][col] == '.' and dp[0][col - 1]:
            dp[0][col] = True
    
    # Fill in the first column
    for row in range(1, rows):
        if maze[row][0] == '.' and dp[row - 1][0]:
            dp[row][0] = True
    
    # Fill in the rest of the grid
    for row in range(1, rows):
        for col in range(1, cols):
            if maze[row][col] == '.' and (dp[row - 1][col] or dp[row][col - 1]):
                dp[row][col] = True
    
    return dp[rows - 1][cols - 1]