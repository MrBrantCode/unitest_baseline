"""
QUESTION:
Construct a function `construct_matrix` that creates and returns a 2-dimensional array of zeros with a specified number of rows and columns. The function should take two parameters: `rows` and `cols`, representing the number of rows and columns in the matrix, respectively.
"""

def construct_matrix(rows, cols):
    return [[0] * cols for _ in range(rows)]