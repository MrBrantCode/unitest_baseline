"""
QUESTION:
Write a function `find_max_path_sum` that takes a 2D array of positive integers as input and returns the maximum sum of a path from the top left cell to the bottom right cell. The path can only move downwards or rightwards, and each cell can only be visited once. The function should not take any other inputs.
"""

def find_max_path_sum(grid):
    rows = len(grid)
    cols = len(grid[0])

    # Create dp array
    dp = [[0] * cols for _ in range(rows)]

    # Initialize the top left cell of dp array
    dp[0][0] = grid[0][0]

    # Fill the first row of dp array
    for j in range(1, cols):
        dp[0][j] = dp[0][j-1] + grid[0][j]

    # Fill the first column of dp array
    for i in range(1, rows):
        dp[i][0] = dp[i-1][0] + grid[i][0]

    # Fill the rest of the dp array
    for i in range(1, rows):
        for j in range(1, cols):
            dp[i][j] = max(dp[i-1][j], dp[i][j-1]) + grid[i][j]

    # Return the maximum sum of a path
    return dp[-1][-1]