"""
QUESTION:
Write a function `transpose_matrix(matrix)` that takes a 2D array (square matrix) of binary numbers as strings and returns the transposed matrix with the binary numbers converted to their corresponding decimal values. The function should have a time complexity of O(n^2) and a space complexity of O(n), where n is the size of the input matrix.
"""

def transpose_matrix(matrix):
    n = len(matrix)
    transposed = [[0] * n for _ in range(n)]  # Initialize the transposed matrix with zeros
    
    for i in range(n):
        for j in range(n):
            binary = matrix[j][i]  # Extract the binary number at (i, j)
            decimal = int(binary, 2)  # Convert the binary number to decimal
            transposed[i][j] = decimal  # Set the decimal number at (j, i) in the transposed matrix
            
    return transposed