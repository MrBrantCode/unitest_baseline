"""
QUESTION:
Design a function called `matrix_dimensions` that takes in a matrix as input, where the matrix is a 2D list containing integers, floats, and strings, and is guaranteed to have at least one row and one column. The function should return a tuple containing the number of rows and the number of columns in each row. If all rows have the same number of columns, the number of columns should be returned as an integer; otherwise, it should be returned as a list of integers.
"""

def matrix_dimensions(matrix):
    rows = len(matrix)
    columns = [len(row) for row in matrix]
    if len(set(columns)) == 1:
        columns = columns[0]
    return rows, columns