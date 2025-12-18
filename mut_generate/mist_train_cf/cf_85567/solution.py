"""
QUESTION:
Write a function `swap_elements(matrix)` that swaps the first and last elements of a given matrix, as well as the first and last elements of each row within the matrix. The function should be able to handle both square and rectangular matrices. The input matrix is valid if it is a list of lists where each inner list has the same length. If the input matrix is not valid, the function should return an error message indicating the issue. The function should also handle empty matrices.
"""

def swap_elements(matrix):
    """
    This function swaps the first and last elements of a given matrix, 
    as well as the first and last elements of each row within the matrix.

    Args:
    matrix (list of lists): A list of lists where each inner list has the same length.

    Returns:
    list of lists: The modified matrix with the first and last elements swapped.
    str: An error message if the input matrix is not valid.
    """
    
    # Check if the input matrix is valid
    if not isinstance(matrix, list):
        return "The input should be a list."
    for row in matrix:
        if not isinstance(row, list):
            return "All elements in the matrix should be lists."
        if len(row) != len(matrix[0]):
            return "All rows should have the same number of elements."
    
    # Handle empty matrices
    if len(matrix) == 0 or len(matrix[0]) == 0:
        return matrix

    # Swap rows
    matrix[0], matrix[-1] = matrix[-1], matrix[0]

    # Swap elements of each row
    for i in range(len(matrix)):
        matrix[i][0], matrix[i][-1] = matrix[i][-1], matrix[i][0]

    return matrix