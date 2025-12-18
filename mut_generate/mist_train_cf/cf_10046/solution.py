"""
QUESTION:
Implement a function `calculate_determinant` that takes a 3x3 matrix as input and returns its determinant without using any built-in matrix operations or libraries. The input matrix is a list of lists, where each inner list represents a row of the matrix, and the elements are numbers.
"""

def calculate_determinant(matrix):
    a, b, c = matrix[0]
    d, e, f = matrix[1]
    g, h, i = matrix[2]
    
    return a*(e*i - f*h) - b*(d*i - f*g) + c*(d*h - e*g)