"""
QUESTION:
Implement a function `matrix_addition(matrix1, matrix2)` that adds two sparse matrices represented as two-dimensional arrays. The input matrices have the same number of rows and columns, and the function should return the result matrix with a time complexity of O(n), where n is the total number of non-zero elements in the matrices, and a space complexity of O(m + n), where m is the number of rows and n is the number of columns.
"""

def matrix_addition(matrix1, matrix2):
    rows = len(matrix1)
    cols = len(matrix1[0])
    
    result = [[0 for _ in range(cols)] for _ in range(rows)]
    
    for i in range(rows):
        for j in range(cols):
            result[i][j] = matrix1[i][j] + matrix2[i][j]
            
    return result