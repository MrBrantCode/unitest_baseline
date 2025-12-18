"""
QUESTION:
Implement the function `unique_paths_with_obstacles(obstacle_grid: List[List[int]]) -> int` that calculates the total number of unique paths to reach the bottom-right corner of a grid from the top-left corner, where movement is restricted to down or right and 1 in the grid represents an obstacle and 0 represents an empty cell. The function should return 0 if there is an obstacle at the top-left or bottom-right corner.
"""

from typing import List

def unique_paths_with_obstacles(obstacle_grid: List[List[int]]) -> int:
    if obstacle_grid[0][0] == 1 or obstacle_grid[-1][-1] == 1:
        return 0

    m, n = len(obstacle_grid), len(obstacle_grid[0])
    dp = [[0] * n for _ in range(m)]

    dp[0][0] = 1 - obstacle_grid[0][0]

    for i in range(1, m):
        dp[i][0] = dp[i-1][0] * (1 - obstacle_grid[i][0])

    for j in range(1, n):
        dp[0][j] = dp[0][j-1] * (1 - obstacle_grid[0][j])

    for i in range(1, m):
        for j in range(1, n):
            if obstacle_grid[i][j] == 0:
                dp[i][j] = dp[i-1][j] + dp[i][j-1]

    return dp[-1][-1]