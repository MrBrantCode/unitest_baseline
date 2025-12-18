"""
QUESTION:
Write a function `multiply_matrices(matrixA, matrixB)` that takes two 2D arrays (matrices) as input and returns their product. The function should handle matrices of any size, assuming they are compatible for multiplication. The function should not use any external libraries.
"""

def multiply_matrices(matrixA, matrixB): 
    """
    Matrix multiplication
    :param matrixA: 2D array
    :param matrixB: 2D array
    :return: product of matrixA and matrixB
    """
    
    # Initialize matrix to store the result with size (m x n), where m and n are the rows and columns of matrixA and matrixB
    result_matrix = [[0 for _ in range(len(matrixB[0]))] for _ in range(len(matrixA))]

    for i in range(len(matrixA)): 
        for j in range(len(matrixB[0])): 
            for k in range(len(matrixB)): 
                result_matrix[i][j] += matrixA[i][k] * matrixB[k][j] 
  
    return result_matrix