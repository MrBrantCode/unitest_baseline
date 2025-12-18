"""
QUESTION:
Create a function `matrix_multiply(matrix1, matrix2)` that takes two 2D lists (matrices) as input and returns their product. The function should check if the number of columns in `matrix1` is equal to the number of rows in `matrix2`. If not, it should return an error message. The function should return the result as a 2D list where each element at position [i][j] is the sum of the products of the elements from row i of `matrix1` and column j of `matrix2`.
"""

def matrix_multiply(matrix1, matrix2):
    """
    This function multiplies two matrices.
    
    Args:
    matrix1 (list): The first matrix.
    matrix2 (list): The second matrix.
    
    Returns:
    list: The product of the two input matrices. If the matrices cannot be multiplied, it returns an error message.
    """
    if len(matrix1[0]) != len(matrix2):
        return "Matrices should have the same size for multiplication"
    result = [[0 for _ in range(len(matrix2[0]))] for _ in range(len(matrix1))]
    for i in range(len(matrix1)):
        for j in range(len(matrix2[0])):
            for k in range(len(matrix2)):
                result[i][j] += matrix1[i][k] * matrix2[k][j]
    return result