"""
QUESTION:
Design a function `create_sparse_matrix` to efficiently represent a sparse matrix with a large number of rows and columns (billions) where the number of non-zero elements is less than 0.1% of the total elements. The function should minimize memory consumption and allow for efficient random access and matrix operations.
"""

import numpy as np

def create_sparse_matrix(num_rows, num_cols, non_zero_elements):
    """
    Creates a sparse matrix in the Compressed Sparse Row (CSR) format.

    Args:
    num_rows (int): The number of rows in the sparse matrix.
    num_cols (int): The number of columns in the sparse matrix.
    non_zero_elements (list): A list of tuples containing the row index, column index, and value of each non-zero element.

    Returns:
    values (numpy.ndarray): The values array of the CSR format, containing the non-zero elements of the matrix.
    col_indices (numpy.ndarray): The column indices array of the CSR format, storing the column index for each non-zero element.
    row_pointers (numpy.ndarray): The row pointer array of the CSR format, indicating the starting index in the values array for each row.
    """
    
    # Initialize the values and column indices arrays
    values = np.zeros(len(non_zero_elements))
    col_indices = np.zeros(len(non_zero_elements), dtype=int)

    # Initialize the row pointers array
    row_pointers = np.zeros(num_rows + 1, dtype=int)

    # Populate the values and column indices arrays
    for i, (row, col, val) in enumerate(non_zero_elements):
        values[i] = val
        col_indices[i] = col

    # Populate the row pointers array
    row_counts = np.bincount([x[0] for x in non_zero_elements], minlength=num_rows)
    row_pointers[1:] = np.cumsum(row_counts)

    return values, col_indices, row_pointers