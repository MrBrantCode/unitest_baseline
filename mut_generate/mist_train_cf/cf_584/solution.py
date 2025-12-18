"""
QUESTION:
Write a function `multiply_matrices(matrix1, matrix2)` that multiplies two matrices. The function should return the resulting matrix if the multiplication is possible; otherwise, it should return `None`. 

The dimensions of the input matrices can be any positive integers, and the elements are integers in the range [-100, 100]. The resulting matrix should have dimensions (m, n), where m is the number of rows in `matrix1` and n is the number of columns in `matrix2`. The function should have a time complexity of O(m * n * p), where p is the number of columns in `matrix1` (which is also the number of rows in `matrix2`).
"""

def multiply_matrices(matrix1, matrix2):
    if len(matrix1[0]) != len(matrix2):
        return None
    
    m = len(matrix1)
    n = len(matrix2[0])
    result = [[0] * n for _ in range(m)]
    
    for i in range(m):
        for j in range(n):
            for k in range(len(matrix2)):
                result[i][j] += matrix1[i][k] * matrix2[k][j]
    
    return result