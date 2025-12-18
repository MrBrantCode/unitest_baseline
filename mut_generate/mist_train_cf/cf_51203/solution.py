"""
QUESTION:
Write a function `maxProductPath` that takes a 2D grid of integers as input and returns the maximum non-negative product of all integers in the grid cells visited along a path from the top-left corner to the bottom-right corner. The product of a path is the product of all integers in the grid cells visited along the path. If the maximum product is negative, return -1. The product should be modulo `10^9 + 7`. 

The function should have the following restrictions:
- The input grid will have at least 1 row and 1 column, and at most 20 rows and 20 columns.
- The integers in the grid will be between -10 and 10 (inclusive).
- In each step, you can only move right, down, or diagonally (right-down) in the matrix.
"""

def maxProductPath(grid):
    """
    This function calculates the maximum non-negative product of all integers in the grid cells 
    visited along a path from the top-left corner to the bottom-right corner.

    Parameters:
    grid (list): A 2D grid of integers.

    Returns:
    int: The maximum non-negative product modulo 10^9 + 7. If the maximum product is negative, return -1.
    """
    MOD = 10**9 + 7
    rows, cols = len(grid), len(grid[0])
    dp = [[None]*cols for _ in range(rows)]
    dp[0][0] = (grid[0][0], grid[0][0])  # maxProd, minProd
        
    # populate first row
    for j in range(1, cols):
        dp[0][j] = (dp[0][j-1][0]*grid[0][j]%MOD, dp[0][j-1][1]*grid[0][j])
        
    # populate first column
    for i in range(1, rows):
        dp[i][0] = (dp[i-1][0][0]*grid[i][0]%MOD, dp[i-1][0][1]*grid[i][0])

    # populate rest of the dp array
    for i in range(1, rows):
        for j in range(1, cols):
            nums = [dp[i-1][j][0]*grid[i][j], dp[i-1][j][1]*grid[i][j], 
                dp[i][j-1][0]*grid[i][j], dp[i][j-1][1]*grid[i][j]]
            dp[i][j] = (max(nums)%MOD, min(nums))
        
    maxVal = dp[-1][-1][0]
    return maxVal if maxVal >= 0 else -1