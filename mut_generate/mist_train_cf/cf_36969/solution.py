"""
QUESTION:
Write a function `maxSumPath(grid: List[List[int]]) -> int` to find the maximum sum of integers that can be obtained by traversing from the top-left cell to the bottom-right cell, moving only right or down at each step, in a given grid of non-negative integers of size n x m.

The function takes a 2D list `grid` representing the grid of non-negative integers as input, where 1 <= n, m <= 100, and each cell contains a non-negative integer value between 0 and 1000. The function should return an integer representing the maximum sum of integers that can be obtained by following the specified traversal rules.
"""

from typing import List

def maxSumPath(grid: List[List[int]]) -> int:
    n = len(grid)
    m = len(grid[0])

    # Initialize the first row
    for j in range(1, m):
        grid[0][j] += grid[0][j-1]

    # Initialize the first column
    for i in range(1, n):
        grid[i][0] += grid[i-1][0]

    # Calculate the maximum sum path
    for i in range(1, n):
        for j in range(1, m):
            grid[i][j] += max(grid[i-1][j], grid[i][j-1])

    return grid[n-1][m-1]