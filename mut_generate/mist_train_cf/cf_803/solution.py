"""
QUESTION:
Write a function `product_of_matrix(matrix)` that calculates the product of all elements in a given matrix of integers. If any element in the matrix is zero or negative, the function should return -1. The function should be able to handle matrices with up to 1000 rows and 1000 columns.
"""

def product_of_matrix(matrix):
    rows = len(matrix)
    columns = len(matrix[0])
    
    product = 1
    
    for i in range(rows):
        for j in range(columns):
            if matrix[i][j] <= 0:
                return -1
            product *= matrix[i][j]
    
    return product