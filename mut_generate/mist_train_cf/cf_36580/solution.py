"""
QUESTION:
Write a function `uniquePaths` that takes two integers `m` and `n` representing the number of rows and columns in a grid, and returns the number of unique paths a robot can take to reach the bottom-right corner from the top-left corner, where the robot can only move down or right. The function should not take any other inputs and should return the result as an integer.
"""

def uniquePaths(m: int, n: int) -> int:
    # Create a 2D array to store the number of unique paths for each cell
    dp = [[1] * n for _ in range(m)]

    # Fill the array with the number of unique paths
    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = dp[i-1][j] + dp[i][j-1]

    return dp[m-1][n-1]