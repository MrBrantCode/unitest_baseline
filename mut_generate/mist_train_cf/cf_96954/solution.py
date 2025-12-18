"""
QUESTION:
Create a function `multiply_matrices` that takes two 4x4 matrices as input and returns their product. The input matrices are represented as lists of lists, where each inner list represents a row in the matrix. The function should multiply the corresponding elements of each row of the first matrix with the corresponding elements of each column of the second matrix and sum the results. The function should return the resulting 4x4 matrix.
"""

def multiply_matrices(mat1, mat2):
    """
    This function multiplies two 4x4 matrices.

    Args:
        mat1 (list): The first 4x4 matrix.
        mat2 (list): The second 4x4 matrix.

    Returns:
        list: The product of the two input matrices.
    """
    # Initialize the result matrix with zeros
    result = [[0,0,0,0],
              [0,0,0,0],
              [0,0,0,0],
              [0,0,0,0]]

    # Perform matrix multiplication
    for i in range(len(mat1)):
        for j in range(len(mat2[0])):
            for k in range(len(mat2)):
                result[i][j] += mat1[i][k] * mat2[k][j]

    return result