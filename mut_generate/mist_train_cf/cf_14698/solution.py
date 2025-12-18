"""
QUESTION:
Create a function `add_matrices` that takes two 2D integer matrices as input and returns a new matrix that is the sum of the input matrices. The function should have the following properties:

- It should check if the input matrices have equal sizes and return an error message if they do not.
- It should handle cases where the input matrices have a maximum size of 1000x1000.
- It should check for possible integer overflow when performing the addition and return an error message if an overflow occurs.
- It should have a time complexity of O(n^2), where n is the size of the matrices.

The function should return a new matrix containing the sum of the input matrices if successful, or an error message as a string otherwise.
"""

def add_matrices(matrix1, matrix2):
    if len(matrix1) != len(matrix2) or len(matrix1[0]) != len(matrix2[0]):
        return "Error: Matrices must have equal sizes."
    
    rows = len(matrix1)
    cols = len(matrix1[0])
    
    result = [[0] * cols for _ in range(rows)]
    
    for i in range(rows):
        for j in range(cols):
            try:
                result[i][j] = matrix1[i][j] + matrix2[i][j]
            except OverflowError:
                return "Error: Integer overflow occurred during addition."
    
    return result