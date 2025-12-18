"""
QUESTION:
Write a function `max_path_sum` that takes a 2D array `grid` of integers as input and returns the maximum sum of numbers that can be obtained by tracing a path from the top-left to the bottom-right corner, where you can only move down or right at each step. The function should not take any additional arguments.
"""

def max_path_sum(grid):
    n = len(grid)
    m = len(grid[0])
    
    dp = [[0] * m for _ in range(n)]
    
    dp[0][0] = grid[0][0]
    
    for j in range(1, m):
        dp[0][j] = dp[0][j-1] + grid[0][j]
    
    for i in range(1, n):
        dp[i][0] = dp[i-1][0] + grid[i][0]
    
    for i in range(1, n):
        for j in range(1, m):
            dp[i][j] = max(dp[i-1][j], dp[i][j-1]) + grid[i][j]
    
    return dp[n-1][m-1]