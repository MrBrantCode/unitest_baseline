"""
QUESTION:
Write a function named `multiply_matrices` that takes two 3x3 matrices as input and returns their product. The function should not use any built-in matrix multiplication functions.
"""

def multiply_matrices(matrix1, matrix2):
    """
    This function takes two 3x3 matrices as input and returns their product.
    
    Args:
        matrix1 (list): The first 3x3 matrix.
        matrix2 (list): The second 3x3 matrix.
    
    Returns:
        list: The product of matrix1 and matrix2.
    """
    
    # initialize an empty matrix to hold the result of the multiplication
    result_matrix = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

    # iterate through each row of the first matrix
    for i in range(len(matrix1)):
        # iterate through each column of the second matrix
        for j in range(len(matrix2[0])):
            # iterate through each element of the first matrix's row
            for k in range(len(matrix1[0])):
                # multiply and add the corresponding elements from each matrix
                result_matrix[i][j] += matrix1[i][k] * matrix2[k][j]

    return result_matrix