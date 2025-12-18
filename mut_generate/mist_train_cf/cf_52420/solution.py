"""
QUESTION:
Write a function named `calc_det(matrix)` that calculates the determinant of a given N x N matrix recursively without using built-in functions for the calculation. The function should handle potential input errors such as non-square matrix and non-numeric elements. The matrix is represented as a list of lists in Python, where each inner list represents a row of the matrix. The function should return the determinant value if the input is valid, otherwise return an error message.
"""

def calc_det(matrix):
    """
    This function calculates the determinant of a given N x N matrix recursively.
    
    Parameters:
    matrix (list of lists): A 2D list representing the matrix.
    
    Returns:
    int/float: The determinant of the matrix.
    str: An error message if the input is invalid.
    """

    # Check for input errors
    try:
        N = len(matrix)
        for row in matrix:
            if len(row) != N:                # Checking for non-square matrix
                return "Error: Non-Square Matrix"
            for element in row:              # Checking for non-numeric elements
                if not isinstance(element,(int, float)):
                    return "Error: Non-Numeric Elements Found"
    except TypeError:
        return 'Error: Input must be a list of lists'

    # Base case for recursion
    if len(matrix) == 2 and len(matrix[0]) == 2: 
        val = matrix[0][0] * matrix[1][1] - matrix[1][0] * matrix[0][1]
        return val

    # Create sub-matrix function
    def create_sub_matrix(mtrx, exclude_row, exclude_col):
        return [[mtrx[i][j] for j in range(len(mtrx[i])) if j != exclude_col] 
                for i in range(len(mtrx)) if i != exclude_row]
    
    # Recursive case
    total = 0 
    index = list(range(len(matrix)))
    for fc in index: 
        sign = (-1) ** (fc % 2) 
        sub_det = calc_det(create_sub_matrix(matrix, 0, fc))
        total += sign * matrix[0][fc] * sub_det 
        
    return total