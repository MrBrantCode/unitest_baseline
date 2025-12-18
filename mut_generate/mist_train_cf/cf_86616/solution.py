"""
QUESTION:
Write a function called `product_of_matrix` that takes a 2D list of integers as input and returns the product of all its elements. If any element in the matrix is zero or negative, the function should return -1. The function should be able to handle matrices with up to 1000 rows and 1000 columns.
"""

def product_of_matrix(matrix):
    product = 1
    
    for row in matrix:
        for element in row:
            if element <= 0:
                return -1
            product *= element
    
    return product