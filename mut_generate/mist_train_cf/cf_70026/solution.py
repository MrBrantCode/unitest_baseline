"""
QUESTION:
Write a recursive function `product_of_elements(matrix)` to calculate the product of all non-zero elements in a given matrix. The matrix can be of any shape, contain negative numbers, and have zeros. The function should return the product of all non-zero elements.
"""

def product_of_elements(matrix):
    # Base case: If the matrix is empty, return 1
    if len(matrix) == 0:
        return 1
    else:
        row = matrix[0] # First (current) row of the matrix
        rest_matrix = matrix[1:] # Rest of the matrix
        product = 1
        for i in row: 
            if i != 0:
                product *= i # Multiply only non-zero elements
        # Recursively calculate the rest of the product
        return product * product_of_elements(rest_matrix)