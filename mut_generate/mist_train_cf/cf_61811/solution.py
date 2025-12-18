"""
QUESTION:
Create a function `add_matrices` that takes two 2D lists (matrices) as input and returns their sum. The matrices are only addable if they have the same number of rows and columns. If the matrices are not the same size, the function should print an error message and return `None`. Otherwise, it should return a new 2D list representing the sum of the input matrices. The function should not modify the input matrices.
"""

def add_matrices(matrix1, matrix2):
    """
    Adds two 2D lists (matrices) if they have the same number of rows and columns.
    
    Args:
        matrix1 (list): The first matrix.
        matrix2 (list): The second matrix.
    
    Returns:
        list or None: The sum of the input matrices if they are the same size, otherwise None.
    """
    
    # Check if the matrices have the same dimensions
    if len(matrix1) != len(matrix2) or len(matrix1[0]) != len(matrix2[0]):
        print("Matrices are not the same size, can not perform addition")
        return None
    
    # Perform addition
    result = [[0 for _ in range(len(matrix1[0]))] for _ in range(len(matrix1))]
    
    # Iterate through rows
    for i in range(len(matrix1)):   
       # Iterate through columns
       for j in range(len(matrix1[0])):
           result[i][j] = matrix1[i][j] + matrix2[i][j]
    
    return result