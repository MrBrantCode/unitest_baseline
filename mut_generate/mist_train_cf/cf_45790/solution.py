"""
QUESTION:
Write a function `spiral_matrix` that takes a 2D matrix (a list of lists) as input and returns a list of elements in spiral order, starting from the top left corner. The function should work with matrices of any dimensions (including non-square matrices) and assume that all inner lists (rows) are of equal length.
"""

def spiral_matrix(matrix):
    result = []
    while matrix:
        # Right
        if matrix:
            result += matrix.pop(0)
        # Down
        if matrix and matrix[0]:
            for row in matrix:
                result.append(row.pop())
        # Left
        if matrix:
            result += matrix.pop()[::-1]
        # Up
        if matrix and matrix[0]:
            for row in matrix[::-1]:
                result.append(row.pop(0))
    return result