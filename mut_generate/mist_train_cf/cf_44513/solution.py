"""
QUESTION:
Create a function called `swap_first_last(matrix)` that takes a 2D list (matrix) as an argument. The function should swap the first and last elements of the matrix, if the matrix is not empty and contains at least one row and one column.
"""

def swap_first_last(matrix):
    if len(matrix) > 0 and len(matrix[0]) > 0:
        matrix[0][0], matrix[-1][-1] = matrix[-1][-1], matrix[0][0]
    return matrix