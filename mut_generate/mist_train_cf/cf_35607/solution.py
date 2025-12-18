"""
QUESTION:
You are given a grid of size m x n, where each cell contains a non-negative integer value. You are initially positioned at the top-left cell and are required to reach the bottom-right cell. You can only move either down or right at any point in time. 

Write a function `minPathSum(grid)` to calculate the minimum sum of values along a path from the top-left cell to the bottom-right cell. The function takes a 2D list of integers as input and returns an integer representing the minimum sum.
"""

from typing import List

def minPathSum(grid: List[List[int]]) -> int:
    m, n = len(grid), len(grid[0])
    
    # Initialize the first row
    for j in range(1, n):
        grid[0][j] += grid[0][j-1]
    
    # Initialize the first column
    for i in range(1, m):
        grid[i][0] += grid[i-1][0]
    
    # Calculate the minimum sum path for each cell
    for i in range(1, m):
        for j in range(1, n):
            grid[i][j] += min(grid[i-1][j], grid[i][j-1])
    
    return grid[-1][-1]