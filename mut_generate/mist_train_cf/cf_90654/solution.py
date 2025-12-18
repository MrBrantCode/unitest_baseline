"""
QUESTION:
Create a function `initialize_matrix` that takes two parameters, `rows` and `cols`, representing the dimensions of a matrix. The function should use a recursive algorithm to create a matrix with the specified dimensions, filled entirely with zeros.
"""

def initialize_matrix(rows, cols):
    if rows == 0:
        return []
    else:
        return [cols*[0]] + initialize_matrix(rows-1, cols)