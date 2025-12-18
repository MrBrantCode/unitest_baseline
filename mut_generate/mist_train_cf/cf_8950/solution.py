"""
QUESTION:
Create a function called `initialize_matrix` that takes two parameters, `rows` and `cols`, and returns a 2D list (matrix) with the specified number of rows and columns, initialized with all zeros using a recursive algorithm.
"""

def initialize_matrix(rows, cols):
    if rows == 0:
        return []
    else:
        return [cols*[0]] + initialize_matrix(rows-1, cols)