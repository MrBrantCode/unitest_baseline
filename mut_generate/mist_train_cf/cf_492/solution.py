"""
QUESTION:
Write a function `multiply_matrices` that takes two 2D lists `matrix1` and `matrix2` representing n x m matrices, where the number of columns in `matrix1` equals the number of rows in `matrix2`. The function should return a new 2D list representing the product of `matrix1` and `matrix2`. If the input matrices cannot be multiplied, return `None`. Also, calculate the sum of all elements in the resulting matrix and return it along with the result matrix.
"""

def multiply_matrices(matrix1, matrix2):
    """
    This function multiplies two matrices and returns the result along with the sum of its elements.

    Args:
        matrix1 (list): The first matrix.
        matrix2 (list): The second matrix.

    Returns:
        tuple: A tuple containing the resulting matrix and the sum of its elements, or None if the matrices cannot be multiplied.
    """
    rows1 = len(matrix1)
    cols1 = len(matrix1[0])
    rows2 = len(matrix2)
    cols2 = len(matrix2[0])
    
    if cols1 != rows2:
        return None

    result = [[sum(a * b for a, b in zip(row, col)) for col in zip(*matrix2)] for row in matrix1]
    total_sum = sum(sum(row) for row in result)
    
    return result, total_sum