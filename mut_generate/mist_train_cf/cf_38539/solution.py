"""
QUESTION:
Implement a function `isCellEditingAllowed(grid, column)` that determines whether editing a cell in a grid is allowed based on the column index. The function takes a 2D grid array and a column index as input. The rules for allowing cell editing are as follows:
- The column index must be within the range of the grid's columns (0 to the number of columns - 1).
- Editing is allowed if the column index is even.
- Editing is not allowed if the column index is odd.
"""

def isCellEditingAllowed(grid, column):
    num_columns = len(grid[0])
    if column < 0 or column >= num_columns:
        return False
    return column % 2 == 0