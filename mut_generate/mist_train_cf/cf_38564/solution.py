"""
QUESTION:
Write a function `maxPathSum(grid: List[List[int]]) -> int` that takes a 2D grid of non-negative integers as input, where each cell represents a score. The function should return the maximum possible sum of a path from the top-left cell to the bottom-right cell, moving only right or down at each step, and the score gained at each step is equal to the value of the destination cell. The function should have a time complexity of O(m*n), where m and n are the number of rows and columns in the grid, respectively.
"""

from typing import List

def entrance(grid: List[List[int]]) -> int:
    m, n = len(grid), len(grid[0])
    
    # Initialize the first row and first column with cumulative sums
    for i in range(1, m):
        grid[i][0] += grid[i-1][0]
    for j in range(1, n):
        grid[0][j] += grid[0][j-1]
    
    # Calculate cumulative sums for each cell
    for i in range(1, m):
        for j in range(1, n):
            grid[i][j] += max(grid[i-1][j], grid[i][j-1])
    
    return grid[m-1][n-1]