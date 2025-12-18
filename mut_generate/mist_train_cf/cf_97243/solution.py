"""
QUESTION:
Write a function called `multiply_matrices` that takes two matrices as input, multiplies them, and returns the result as a new matrix. The input matrices can have a maximum size of 1000x1000 and contain only integer values. The function should return an error message if the input matrices have incompatible sizes or if an integer overflow occurs during the multiplication. The function should be able to handle non-square matrices.
"""

def multiply_matrices(matrix1, matrix2):
    """
    Multiply two matrices and return the result.
    
    Args:
    matrix1 (list of lists): The first matrix.
    matrix2 (list of lists): The second matrix.
    
    Returns:
    list of lists: The product of the two matrices. If the matrices have incompatible sizes, returns an error message. If an integer overflow occurs during multiplication, returns an error message.
    """
    rows1, cols1 = len(matrix1), len(matrix1[0])
    rows2, cols2 = len(matrix2), len(matrix2[0])

    if cols1 != rows2:
        return "Error: Incompatible sizes for matrix multiplication"

    result = [[0] * cols2 for _ in range(rows1)]

    for i in range(rows1):
        for j in range(cols2):
            for k in range(cols1):
                try:
                    result[i][j] += matrix1[i][k] * matrix2[k][j]
                except OverflowError:
                    return "Error: Integer overflow occurred during multiplication"

    return result