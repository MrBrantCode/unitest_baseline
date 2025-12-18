"""
QUESTION:
Create a function `rotate_matrix_counter_clockwise` that takes a 2D array (matrix) as input and returns the rotated matrix 90 degrees in the counter-clockwise direction. The function should work for any square matrix (i.e., a matrix with the same number of rows and columns).
"""

def rotate_matrix_counter_clockwise(matrix):
    """
    Rotate a square matrix 90 degrees in the counter-clockwise direction.

    Args:
        matrix (list of lists): A 2D array (matrix) with the same number of rows and columns.

    Returns:
        list of lists: The rotated matrix.
    """
    # Transpose the matrix
    transpose_matrix = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]
    
    # Reverse each row
    result = [row[::-1] for row in transpose_matrix]
    
    return result