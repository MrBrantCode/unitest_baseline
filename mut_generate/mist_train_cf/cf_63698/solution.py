"""
QUESTION:
Create a function `matrix_disparity(matrix)` that takes a two-dimensional matrix as input and returns the largest discrepancy between the smallest and largest numerical elements in every component sub-matrix. The sub-matrix is defined as a matrix of any shape contained within the input matrix, with all numbers being contiguous. The input matrix is not guaranteed to be a proper matrix where all rows have the same number of elements.
"""

def matrix_disparity(matrix):
    # Flattening the matrix
    flat_list = [item for sublist in matrix for item in sublist]
    
    return max(flat_list) - min(flat_list)