"""
QUESTION:
Write a function `transpose_and_calculate_product(matrix)` that takes a 2D matrix of integers as input and returns the transposed matrix, the product of each row in the transposed matrix, and the product of each column in the original matrix. The input matrix should contain integers in the range of -1000 to 1000 and have dimensions up to 1000x1000.
"""

def transpose_and_calculate_product(matrix):
    # Transpose the matrix
    transposed_matrix = list(map(list, zip(*matrix)))

    # Calculate the product of each row
    row_products = [product(row) for row in transposed_matrix]

    # Calculate the product of each column
    column_products = [product(column) for column in zip(*matrix)]

    return transposed_matrix, row_products, column_products


def product(numbers):
    result = 1
    for number in numbers:
        result *= number
    return result