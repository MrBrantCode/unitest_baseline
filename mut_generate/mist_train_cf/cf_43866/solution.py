"""
QUESTION:
Write a function `multiply_elements(matrix)` that takes a two-dimensional list of integers as input and returns the product of all elements in the matrix. The input matrix may be empty or contain non-numeric data, but the function should assume it only contains integers or real numbers.
"""

def multiply_elements(matrix):
    result = 1
    for row in matrix:
        for elem in row:
            result *= elem
    return result