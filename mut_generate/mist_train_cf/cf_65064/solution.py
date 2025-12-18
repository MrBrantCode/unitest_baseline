"""
QUESTION:
Write a function `rotate_matrix(matrix)` that takes a 2D list (matrix) as input and returns the matrix rotated 90 degrees counter-clockwise. The function should not modify the original matrix and should only use built-in functions.
"""

def rotate_matrix(matrix):
    return list(zip(*matrix[::-1]))