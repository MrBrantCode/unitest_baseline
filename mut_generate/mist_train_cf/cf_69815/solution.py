"""
QUESTION:
Implement a function named `matrix_power` that takes a square matrix and an exponential value as input, and returns the result of the matrix multiplied by itself the given number of times. The function should follow the rules of matrix multiplication and handle base cases where the exponential value is 0 or 1. The input matrix should be a 2D list of integers, and the exponential value should be a non-negative integer. The function should be optimized for efficiency to handle large matrices.
"""

def matrix_power(matrix, n, power):
    """
    This function calculates the power of a square matrix.

    Args:
    matrix (list): A 2D list representing a square matrix.
    n (int): The size of the square matrix.
    power (int): The power to which the matrix should be raised.

    Returns:
    list: The result of the matrix raised to the given power.
    """
    
    # Base case: power is 0, return the identity matrix
    if power == 0:
        return [[1 if row == col else 0 for col in range(n)] for row in range(n)]
    
    # Base case: power is 1, return the input matrix itself
    if power == 1:
        return matrix

    result = matrix.copy()

    # Multiply the matrix by itself 'power' times
    for _ in range(2, power+1):
        tempResult = [[0 for _ in range(n)] for _ in range(n)]
        for i in range(n):
            for j in range(n):
                for k in range(n):
                    tempResult[i][j] += result[i][k] * matrix[k][j]
        result = tempResult 
        
    return result