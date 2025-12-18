"""
QUESTION:
Write a function `product_matrix` that calculates the product of all elements in a given 2D matrix. The input matrix is a list of lists of integers. The function should return the product of all the integers in the matrix.
"""

def product_matrix(matrix):
    product = 1
    for row in matrix:
        for value in row:
            product *= value
    return product