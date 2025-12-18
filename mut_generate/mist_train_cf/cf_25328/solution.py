"""
QUESTION:
Write a function `multiply_matrices` that takes two 2x2 matrices as input and returns their product. The matrices are represented as lists of lists, where each inner list represents a row in the matrix. The input matrices will only contain integers, and the function should return a new 2x2 matrix containing the product of the input matrices.
"""

def multiply_matrices(a, b):
    """
    This function multiplies two 2x2 matrices.
    
    Args:
        a (list): The first 2x2 matrix.
        b (list): The second 2x2 matrix.
    
    Returns:
        list: The product of the two input matrices.
    """
    return [[a[0][0]*b[0][0] + a[0][1]*b[1][0], a[0][0]*b[0][1] + a[0][1]*b[1][1]], 
            [a[1][0]*b[0][0] + a[1][1]*b[1][0], a[1][0]*b[0][1] + a[1][1]*b[1][1]]]