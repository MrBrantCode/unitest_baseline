"""
QUESTION:
Write a function `multiplyMatrix(A, B)` that takes two matrices `A` and `B` as input and returns their product. The function should check if the matrices can be multiplied (i.e., the number of columns in `A` is equal to the number of rows in `B`) and return an error message if they cannot be multiplied. The function should return the product matrix if the multiplication is possible. The input matrices `A` and `B` are represented as lists of lists in Python, where each inner list represents a row in the matrix.
"""

def multiplyMatrix(A, B):
    """
    This function calculates the product of two matrices A and B.

    Args:
    A (list of lists): The first matrix.
    B (list of lists): The second matrix.

    Returns:
    list of lists: The product matrix if the multiplication is possible. Otherwise, it prints an error message and returns None.
    """

    rowsA = len(A)
    colsA = len(A[0])
    rowsB = len(B)
    colsB = len(B[0])

    if colsA != rowsB:
        print("Cannot multiply the two matrices. Incorrect dimensions.")
        return None

    # Create an empty product matrix C[rowA][colB]
    C = [[0 for row in range(colsB)] for col in range(rowsA)]

    # Multiply and fill in the product matrix
    for i in range(rowsA):
        for j in range(colsB):
            for k in range(colsA):
                C[i][j] += A[i][k] * B[k][j]

    return C