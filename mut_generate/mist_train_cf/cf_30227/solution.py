"""
QUESTION:
Write a function `unique_paths` that takes a tuple `input_shape` representing the dimensions of a grid (number of rows and number of columns) as input and returns the number of unique paths from the top-left corner to the bottom-right corner, assuming you can only move down or right. The input grid dimensions are at least 1x1.
"""

def unique_paths(input_shape):
    m, n = input_shape
    dp = [[1] * n for _ in range(m)]

    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = dp[i-1][j] + dp[i][j-1]

    return dp[m-1][n-1]