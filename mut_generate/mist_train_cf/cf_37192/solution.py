"""
QUESTION:
Given a 2D grid of non-negative integers representing the cost of moving through each cell, write a function `minPathSum(grid)` that returns the minimum sum of a path from the top-left cell to the bottom-right cell, moving only right or down. The input grid is a list of lists of integers, where each inner list represents a row in the grid. The function should return an integer representing the minimum path sum.
"""

def minPathSum(grid):
    m, n = len(grid), len(grid[0])
    dp = [[0] * n for _ in range(m)]
    
    dp[0][0] = grid[0][0]
    
    for i in range(1, m):
        dp[i][0] = dp[i-1][0] + grid[i][0]
    
    for j in range(1, n):
        dp[0][j] = dp[0][j-1] + grid[0][j]
    
    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + grid[i][j]
    
    return dp[m-1][n-1]