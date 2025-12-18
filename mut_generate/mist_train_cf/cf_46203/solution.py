"""
QUESTION:
Write a function `maxIncreaseKeepingSkyline` that takes a 2D grid of building heights as input, where `grid[i][j]` represents the height of a building at location `(i, j)`, and returns the maximum cumulative increase in height that can be applied to the buildings without changing the skyline when viewed from all four cardinal directions. The input grid is a square matrix with a size between 1 and 50, and all building heights are integers between 0 and 100.
"""

def maxIncreaseKeepingSkyline(grid):
    maxRows = [max(row) for row in grid]
    maxCols = [max(column) for column in zip(*grid)]
    
    return sum(min(maxRows[i], maxCols[j]) - cell
               for i, row in enumerate(grid)
               for j, cell in enumerate(row))