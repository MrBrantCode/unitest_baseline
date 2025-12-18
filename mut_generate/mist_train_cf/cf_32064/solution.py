"""
QUESTION:
Write a function `count_min_cost_paths(grid)` that takes as input a 2D array `grid` where each cell contains a non-negative integer representing the cost to traverse that cell. The function should return the total number of valid paths from the top-left corner to the bottom-right corner with minimum cost, where a path's cost is the sum of the values of cells visited along the path. Movement is restricted to only right or down at any point in time.
"""

def count_min_cost_paths(grid):
    m, n = len(grid), len(grid[0])
    dp = [[0] * n for _ in range(m)]
    dp[0][0] = 1

    for i in range(1, m):
        dp[i][0] = dp[i-1][0] if grid[i][0] == grid[i-1][0] else 0

    for j in range(1, n):
        dp[0][j] = dp[0][j-1] if grid[0][j] == grid[0][j-1] else 0

    for i in range(1, m):
        for j in range(1, n):
            if grid[i][j] == grid[i-1][j]:
                dp[i][j] += dp[i-1][j]
            if grid[i][j] == grid[i][j-1]:
                dp[i][j] += dp[i][j-1]

    return dp[m-1][n-1]