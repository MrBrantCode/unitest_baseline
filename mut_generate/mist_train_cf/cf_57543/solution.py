"""
QUESTION:
Construct a function named `element_at` that takes a 10x10 two-dimensional matrix and two parameters `i` and `j` as input. The matrix should be composed of 100 unique random numerical elements. The function should return the element located at the (i, j) position in the matrix if it is within bounds, otherwise return `None`. The row and column indices `i` and `j` should be 0-indexed, ranging from 0 to 9.
"""

def element_at(matrix, i, j):
    if (i >= 0 and i < 10) and (j >= 0 and j < 10): 
        return matrix[i][j] # Return the element
    else:  
        return None # None if out of matrix bounds