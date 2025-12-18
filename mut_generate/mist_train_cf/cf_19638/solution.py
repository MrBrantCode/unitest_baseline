"""
QUESTION:
Create a function `access_element(matrix, row, col)` that takes a matrix and row and column indices as input, and returns the element at the specified position in the matrix. The matrix can be stored using different data structures (lists, numpy arrays, or nested lists), and the function should work with any of these data structures. Implement the function to handle cases where the given row or column index exceeds the bounds of the matrix.
"""

def access_element(matrix, row, col):
    if row < len(matrix) and col < len(matrix[0]):
        return matrix[row][col]
    else:
        return None  # or raise an exception/error message