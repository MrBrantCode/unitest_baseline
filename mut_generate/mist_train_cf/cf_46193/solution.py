"""
QUESTION:
Create a function `find_diagonal(matrix)` that takes a binary square matrix as input and returns the longest diagonal with a product of its elements equal to 1. The input matrix must be a square matrix, i.e., the number of rows must be equal to the number of columns. The function should return the diagonal elements if their product equals 1; otherwise, it should return a respective message.
"""

import numpy as np

def find_diagonal(matrix):
    try:
        if matrix.shape[0] != matrix.shape[1]:
            return "The input matrix is not a square matrix."
        primary_diagonal_product = np.prod(np.diagonal(matrix))
        secondary_diagonal_product = np.prod(np.diagonal(np.fliplr(matrix)))
        if primary_diagonal_product == 1:
            return np.diagonal(matrix)                          
        elif secondary_diagonal_product == 1:
            return np.diagonal(np.fliplr(matrix))                 
        else:
            return "There is no diagonal which product is 1."
    except Exception as e:
       return str(e)