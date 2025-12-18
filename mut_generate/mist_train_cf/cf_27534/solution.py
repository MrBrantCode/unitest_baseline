"""
QUESTION:
Write a function `getRightCellValue(matrix, row, k_row_i)` that takes a 2D matrix `matrix` and indices `(row, k_row_i)` as input. The function should return the value of the cell to the right of the given cell if it exists within the matrix bounds; otherwise, return None.
"""

def getRightCellValue(matrix, row, k_row_i):
    if k_row_i + 1 < len(matrix[row]):
        return matrix[row][k_row_i + 1]
    else:
        return None