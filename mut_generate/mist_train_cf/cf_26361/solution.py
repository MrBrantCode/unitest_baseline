"""
QUESTION:
Implement the function `multiply(A, B)` that takes two 2D arrays `A` and `B` as input and returns their matrix product. The input arrays `A` and `B` are square matrices of the same size, and the size of the matrices is not specified. The function should perform the standard matrix multiplication operation and return the resulting matrix.
"""

def multiply(A, B):
    """
    This function takes two 2D arrays A and B as input and returns their matrix product.
    
    Args:
        A (list): A 2D array
        B (list): A 2D array
        
    Returns:
        list: The matrix product of A and B
    """
    # Get the size of the matrices
    n = len(A)
    
    # Initialize the result matrix with zeros
    C = [[0 for _ in range(n)] for _ in range(n)]
    
    # Perform matrix multiplication
    for i in range(n):
        for j in range(n):
            for k in range(n):
                C[i][j] += A[i][k] * B[k][j]
    
    return C