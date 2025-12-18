"""
QUESTION:
Create a method named `maxSumPath` that takes a 2D grid and an integer `k` as input and returns the maximum sum of exactly `k` cells in the grid. The method should start from any cell and proceed to adjacent cells that share an edge, ensuring to remain within the grid's limits. The grid is square with a minimum size of 2x2, and each cell has a unique value in the range of 1 to N*N, where N is the size of the grid.
"""

def maxSumPath(grid, k):
    def helper(i, j, k):
        if k == 0:
            return 0
        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]):
            return float('-inf')
        
        max_val = 0
        
        # Visit all adjacent cells
        max_val = max(max_val, helper(i-1, j, k-1))
        max_val = max(max_val, helper(i+1, j, k-1))
        max_val = max(max_val, helper(i, j-1, k-1))
        max_val = max(max_val, helper(i, j+1, k-1))
        
        return max_val + grid[i][j]

    max_sum = 0
    
    # Start from each cell
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            max_sum = max(max_sum, helper(i, j, k))
    
    return max_sum