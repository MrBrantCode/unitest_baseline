"""
QUESTION:
Develop a function `interpolationSearchMatrix(mtx, y)` that performs a 2D interpolation search on a given matrix `mtx` to find the indexes of the target value `y`. The matrix is sorted both row and column wise, and `y` is guaranteed to be in the matrix. The function should return the indexes of `y` as a tuple.
"""

def interpollationSearchMatrix(mtx, y):
    rows = len(mtx)
    cols = len(mtx[0])
    row_index = 0
    col_index = cols - 1
    while row_index < rows and col_index >= 0:
        if mtx[row_index][col_index] == y:
            return (row_index, col_index)
        elif mtx[row_index][col_index] < y:
            row_index += 1
        else:
            col_index -= 1
    return -1