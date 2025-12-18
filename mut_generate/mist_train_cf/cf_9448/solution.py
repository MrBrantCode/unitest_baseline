"""
QUESTION:
Write a function `compute_product(matrix)` that calculates the product of all elements in a given 2D matrix. If the matrix contains at least one zero, the function should return -1.
"""

def compute_product(matrix):
    product = 1
    zero_found = False
    for row in matrix:
        for element in row:
            if element == 0:
                zero_found = True
                break
            product *= element
        if zero_found:
            break
    if zero_found:
        return -1
    return product