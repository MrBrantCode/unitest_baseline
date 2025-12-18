"""
QUESTION:
Implement a function `unique_paths_with_obstacles(obstacle_grid)` that calculates the total number of unique paths to reach the bottom-right corner of a grid from the top-left corner. The grid is represented by a 2D array `obstacle_grid` where 1 indicates an obstacle and 0 indicates an empty space. You can only move either down or to the right at any point in time. If there is an obstacle at the top-left corner or the bottom-right corner, the function should return 0.
"""

from typing import List

def unique_paths_with_obstacles(obstacle_grid: List[List[int]]) -> int:
    m, n = len(obstacle_grid), len(obstacle_grid[0])
    
    if obstacle_grid[0][0] == 1 or obstacle_grid[m-1][n-1] == 1:
        return 0
    
    dp = [[0] * n for _ in range(m)]
    
    dp[0][0] = 1
    
    for i in range(m):
        for j in range(n):
            if obstacle_grid[i][j] == 1:
                dp[i][j] = 0
            else:
                if i > 0:
                    dp[i][j] += dp[i-1][j]
                if j > 0:
                    dp[i][j] += dp[i][j-1]
    
    return dp[m-1][n-1]