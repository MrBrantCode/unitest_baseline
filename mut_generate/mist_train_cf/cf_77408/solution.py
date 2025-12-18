"""
QUESTION:
Write a function `calculate_tridimensional_matrix_product` that calculates the product of each individual element in a given tridimensional matrix. The matrix is a 3D list of integers, and the function should return the product of all elements. Note that if the matrix contains a zero, the product will be zero.
"""

def calculate_tridimensional_matrix_product(matrix):
    """
    This function calculates the product of each individual element in a given tridimensional matrix.

    Args:
    matrix (list): A 3D list of integers.

    Returns:
    int: The product of all elements in the matrix.
    """
    product = 1
    for block in matrix:
        for row in block:
            for num in row:
                product *= num
    return product