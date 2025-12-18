"""
QUESTION:
Design a function `find_longest_diagonal(matrix)` that takes a 2D numpy array as input and returns the longest diagonal from the top left to the bottom right or from the top right to the bottom left of the matrix, whose elements, when cumulatively multiplied, yield a product that equals one. The function should not check diagonals within nested sub-matrices.
"""

import numpy as np

def find_longest_diagonal(matrix):
    # Get the shape of the matrix
    nrows, ncols = matrix.shape

    # Initialize the longest diagonal and its product as none
    longest_diagonal = None
    longest_diagonal_len = 0

    for col_start in range(ncols):
        diagonal = np.diagonal(matrix, offset=col_start)
        diagonal_product = np.prod(diagonal)
        if diagonal_product == 1:
            if len(diagonal) > longest_diagonal_len:
                longest_diagonal_len = len(diagonal)
                longest_diagonal = diagonal

    matrix_flipped = np.fliplr(matrix)
    for col_start in range(ncols):
        diagonal = np.diagonal(matrix_flipped, offset=col_start)
        diagonal_product = np.prod(diagonal)
        if diagonal_product == 1:
            if len(diagonal) > longest_diagonal_len:
                longest_diagonal_len = len(diagonal)
                longest_diagonal = diagonal
                
    return longest_diagonal