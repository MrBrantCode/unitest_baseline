"""
QUESTION:
Implement a function named `create_sparse_matrix` to efficiently represent a sparse matrix with millions of columns and rows. The sparse matrix is expected to have less than 1% non-zero elements. The function should allow for efficient storage, access, and manipulation of the non-zero elements. The function should use the Compressed Sparse Row (CSR) format, which includes three arrays: values, column indices, and row pointers.
"""

import numpy as np

def create_sparse_matrix(num_rows, num_cols, non_zero_elements):
    """
    Creates a sparse matrix using the Compressed Sparse Row (CSR) format.

    Args:
        num_rows (int): The number of rows in the sparse matrix.
        num_cols (int): The number of columns in the sparse matrix.
        non_zero_elements (list of tuples): A list of tuples, where each tuple contains the row index, column index, and value of a non-zero element.

    Returns:
        values (numpy array): The array of non-zero values in the sparse matrix.
        col_indices (numpy array): The array of column indices corresponding to the non-zero values.
        row_pointers (numpy array): The array of row pointers, where each pointer is the starting index in the values array for a row.
    """

    # Sort the non-zero elements by row index
    non_zero_elements.sort(key=lambda x: x[0])

    # Initialize the arrays to store the values, column indices, and row pointers
    values = np.zeros(len(non_zero_elements))
    col_indices = np.zeros(len(non_zero_elements), dtype=int)
    row_pointers = np.zeros(num_rows + 1, dtype=int)

    # Initialize the current row and the index of the next non-zero element in the current row
    current_row = 0
    next_non_zero_index = 0

    # Iterate over the rows
    for i in range(num_rows):
        # Count the number of non-zero elements in the current row
        while next_non_zero_index < len(non_zero_elements) and non_zero_elements[next_non_zero_index][0] == i:
            values[next_non_zero_index] = non_zero_elements[next_non_zero_index][2]
            col_indices[next_non_zero_index] = non_zero_elements[next_non_zero_index][1]
            next_non_zero_index += 1

        # Update the row pointer
        row_pointers[i + 1] = next_non_zero_index

    return values, col_indices, row_pointers