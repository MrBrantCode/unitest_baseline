"""
QUESTION:
Write a function `uniquePaths` that takes a binary matrix `obstacleGrid` as input, where 0 represents an empty space and 1 represents an obstacle, and returns the number of unique paths from the top-left corner to the bottom-right corner modulo 10^9 + 7. The movement is restricted to either down or right at any point in time, and the function should consider the obstacles in the grid.
"""

from typing import List

def uniquePaths(obstacleGrid: List[List[int]]) -> int:
    m, n = len(obstacleGrid), len(obstacleGrid[0])
    dp = [[0] * n for _ in range(m)]
    
    if obstacleGrid[0][0] == 0:
        dp[0][0] = 1
    
    for i in range(m):
        for j in range(n):
            if obstacleGrid[i][j] == 1:
                dp[i][j] = 0
            else:
                if i > 0:
                    dp[i][j] += dp[i-1][j]
                if j > 0:
                    dp[i][j] += dp[i][j-1]
    
    return dp[m-1][n-1] % (10**9 + 7)