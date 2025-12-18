"""
QUESTION:
Write a function `uniquePaths` that takes a 2D grid `maze` as input, where each cell can be either empty (denoted by '.') or blocked (denoted by '#'). The function should return the number of unique paths from the top-left corner to the bottom-right corner, where the player can move either down or right at each step, as long as the destination cell is not blocked. The function should assume that the input maze is a valid grid and the top-left and bottom-right corners are not blocked.
"""

from typing import List

def uniquePaths(maze: List[List[str]]) -> int:
    m, n = len(maze), len(maze[0])
    dp = [[0] * n for _ in range(m)]
    
    # Initialize the first row and column
    for i in range(m):
        if maze[i][0] == '.':
            dp[i][0] = 1
        else:
            break
    for j in range(n):
        if maze[0][j] == '.':
            dp[0][j] = 1
        else:
            break
    
    # Fill in the DP table
    for i in range(1, m):
        for j in range(1, n):
            if maze[i][j] == '.':
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
    
    return dp[m-1][n-1]