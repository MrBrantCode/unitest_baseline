"""
QUESTION:
Write a function `minSumPath(matrix: List[List[int]]) -> int` to calculate the minimum sum path from the top-left cell to the bottom-right cell of a square matrix. The matrix has a size of `n x n` (1 <= n <= 100), where each cell contains a non-negative integer (0 <= matrix[i][j] <= 1000). The function should return an integer representing the minimum sum of costs to reach the bottom-right cell from the top-left cell, considering that you can only move right or down at each step.
"""

from typing import List

def min_sum_path(matrix: List[List[int]]) -> int:
    n = len(matrix)

    # Update the matrix to store the cumulative sum from each cell to the bottom-right cell
    for y in range(n - 2, -1, -1):
        matrix[y][n - 1] += matrix[y + 1][n - 1]
        matrix[n - 1][y] += matrix[n - 1][y + 1]

    for y in range(n - 2, -1, -1):
        for x in range(n - 2, -1, -1):
            matrix[y][x] += min(matrix[y + 1][x], matrix[y][x + 1])

    return matrix[0][0]