"""
QUESTION:
Develop a function named `product_of_matrix` that takes a 2D matrix as input and returns the product of all elements in the matrix. The function should handle the presence of zeros and negative numbers, and should have a minimized time complexity. The input matrix can contain any number of rows and columns.
"""

def product_of_matrix(mat):
    product = 1
    for row in mat:
        for num in row:
            product *= num
    return product