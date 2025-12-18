"""
QUESTION:
Write a function `multiply_matrix(matrix)` that takes a 2D list `matrix` as input and returns the product of all elements in the matrix. Assume the matrix is not empty and contains at least one non-empty list.
"""

def multiply_matrix(matrix):
    result = 1
    for row in matrix:
        for element in row:
            result *= element
    return result