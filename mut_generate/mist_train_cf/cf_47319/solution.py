"""
QUESTION:
Create a function `subtract_matrices(matrix1, matrix2)` that takes two 2D matrices as input and returns a new 2D matrix representing the subtraction of `matrix2` from `matrix1`. The function should check if the input matrices have the same dimensions and return an error message if they do not. If the dimensions match, the function should return a 2D matrix where each element is the difference between the corresponding elements in the input matrices.
"""

def subtract_matrices(matrix1, matrix2):
    """
    This function subtracts two 2D matrices and returns the result.
    
    Args:
        matrix1 (list): The first 2D matrix.
        matrix2 (list): The second 2D matrix.
    
    Returns:
        list: A 2D matrix representing the subtraction of matrix2 from matrix1.
              Returns None if the matrices do not have the same dimensions.
    """

    # Check if matrices have the same dimensions 
    if len(matrix1) != len(matrix2) or len(matrix1[0]) != len(matrix2[0]):
        print("These matrices cannot be subtracted, dimensions do not match")
        return 

    # subtract matrices
    subtracted_matrix = [[matrix1[row][col] - matrix2[row][col] for col in range(len(matrix1[0]))] for row in range(len(matrix1))]

    return subtracted_matrix