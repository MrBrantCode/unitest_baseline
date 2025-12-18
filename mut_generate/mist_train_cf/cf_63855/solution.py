"""
QUESTION:
Write a function `null_space_dimension` to calculate the dimension of the null space of a given matrix. The matrix is a 2D list of integers, and the function should return an integer representing the dimension of the null space. The dimension of the null space can be calculated using the formula n-r, where n is the number of variables (columns in the matrix) and r is the number of leading terms (non-zero rows in the reduced row echelon form of the matrix).
"""

import numpy as np

def null_space_dimension(matrix):
    """
    Calculate the dimension of the null space of a given matrix.

    Args:
        matrix (list): A 2D list of integers representing the matrix.

    Returns:
        int: The dimension of the null space.
    """
    # Convert the input matrix to a NumPy array
    matrix = np.array(matrix, dtype=float)
    
    # Perform row reduction to get the reduced row echelon form of the matrix
    reduced_matrix = np.array(matrix, dtype=float)
    num_rows, num_cols = reduced_matrix.shape
    current_row = 0
    for j in range(num_cols):
        if current_row >= num_rows:
            break
        pivot_row = current_row
        while pivot_row < num_rows and reduced_matrix[pivot_row, j] == 0:
            pivot_row += 1
        if pivot_row == num_rows:
            continue
        reduced_matrix[[current_row, pivot_row]] = reduced_matrix[[pivot_row, current_row]]
        pivot = reduced_matrix[current_row, j]
        reduced_matrix[current_row] = reduced_matrix[current_row] / pivot
        for i in range(num_rows):
            if i == current_row:
                continue
            factor = reduced_matrix[i, j]
            reduced_matrix[i] = reduced_matrix[i] - factor * reduced_matrix[current_row]
        current_row += 1
    
    # Count the number of non-zero rows in the reduced matrix
    num_non_zero_rows = sum(any(row) for row in reduced_matrix)
    
    # Calculate the dimension of the null space using the formula n-r
    null_space_dim = num_cols - num_non_zero_rows
    
    return null_space_dim