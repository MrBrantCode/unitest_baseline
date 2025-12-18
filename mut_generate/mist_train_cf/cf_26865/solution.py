"""
QUESTION:
Write a function `maxSumPath(grid)` that takes a 2D grid of non-negative integers as input, where the path can only move right or down at each step, and returns the maximum sum of a path from the top-left cell to the bottom-right cell.
"""

def maxSumPath(grid):
    rows = len(grid)
    cols = len(grid[0])

    max_sum = [[0] * cols for _ in range(rows)]

    max_sum[0][0] = grid[0][0]

    for j in range(1, cols):
        max_sum[0][j] = max_sum[0][j-1] + grid[0][j]

    for i in range(1, rows):
        max_sum[i][0] = max_sum[i-1][0] + grid[i][0]

    for i in range(1, rows):
        for j in range(1, cols):
            max_sum[i][j] = max(max_sum[i-1][j], max_sum[i][j-1]) + grid[i][j]

    return max_sum[rows-1][cols-1]