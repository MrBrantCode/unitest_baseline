"""
QUESTION:
Write a function `min_cost_path(cost)` that takes a 2D list `cost` representing the cost of traveling through a grid, where each cell `cost[i][j]` represents the cost of traveling to that cell. You can only move right or down in the grid. The function should return the minimum cost to reach the bottom-right cell from the top-left cell. The grid size can be any positive number of rows and columns.
"""

def min_cost_path(cost):
    m, n = len(cost), len(cost[0])
    dp = [[0] * n for _ in range(m)]
    dp[0][0] = cost[0][0]
    for j in range(1, n):
        dp[0][j] = cost[0][j] + dp[0][j-1]
    for i in range(1, m):
        dp[i][0] = cost[i][0] + dp[i-1][0]
    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = cost[i][j] + min(dp[i-1][j], dp[i][j-1])
    return dp[m-1][n-1]