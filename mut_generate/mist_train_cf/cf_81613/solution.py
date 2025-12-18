"""
QUESTION:
Write a function `calculate_product(matrix)` that calculates the product of all numerical elements in a given two-dimensional matrix. The function should iterate through each element in the matrix, considering its position, sequence, and potential duplication, and return the product of all elements. The input matrix is a two-dimensional array where each sub-array represents a row.
"""

def calculate_product(matrix):
    result = 1
    for row in matrix:
        for element in row:
            result *= element
    return result