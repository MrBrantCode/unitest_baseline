"""
QUESTION:
Write a function `max_sum_path(matrix)` that finds a path from the leftmost column to the rightmost column in a given 2D matrix of integers, maximizing the sum of numbers. The path can only move right or down in each step. The function should return the maximum possible sum.
"""

def max_sum_path(matrix):
    rows, columns = len(matrix), len(matrix[0])
    dp = [[float("-inf") for _ in range(columns)] for _ in range(rows)]
    dp[0][0] = matrix[0][0]
    for i in range(rows):
        for j in range(columns):
            if i > 0:
                dp[i][j] = max(dp[i][j], dp[i-1][j] + matrix[i][j])
            if j > 0:
                dp[i][j] = max(dp[i][j], dp[i][j-1] + matrix[i][j])
    return dp[-1][-1]