"""
QUESTION:
Implement a `Grid` class that manages a two-dimensional grid of cells with the following properties and methods:
- The grid has `rows` rows and `cols` columns, with all cells initially set to a default value `default_value`.
- Provide a method `get_cell(row, col)` to access individual cells.
- Provide a method `set_cell(row, col, value)` to modify individual cells.
- Provide a method `count_occurrences(value)` to count the occurrences of a specific value in the entire grid.
- Provide a method `rotate_clockwise()` to rotate the grid by 90 degrees clockwise.
"""

def entance(rows, cols, default_value=0):
    grid = [[default_value for _ in range(cols)] for _ in range(rows)]
    
    def get_cell(row, col):
        return grid[row][col]
    
    def set_cell(row, col, value):
        grid[row][col] = value
    
    def count_occurrences(value):
        count = 0
        for row in grid:
            count += row.count(value)
        return count
    
    def rotate_clockwise():
        nonlocal grid
        grid = [list(row) for row in zip(*grid[::-1])]
    
    return get_cell, set_cell, count_occurrences, rotate_clockwise