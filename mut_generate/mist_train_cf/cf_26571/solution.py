"""
QUESTION:
Create a function `rotate_grid_90_deg(grid)` that takes a grid of characters as input, represented as a list of strings, and returns a new grid that is rotated 90 degrees clockwise. The input grid can be of any size and the function should not modify the original grid. The output grid should be a list of strings, where each string represents a row of the rotated grid.
"""

def rotate_grid_90_deg(grid):
    # Use zip and reversed to rotate the grid 90 degrees clockwise
    rotated = list(zip(*reversed(grid)))
    
    # Convert the rotated grid back to a list of strings
    rotated_grid = ["".join(row) for row in rotated]
    
    return rotated_grid