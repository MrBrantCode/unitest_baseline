"""
QUESTION:
Create a function named `transpose` that takes a 2-dimensional array (or matrix) as input, and returns the transposed matrix. The function should be able to handle arrays of any size, with non-integer elements, sparse arrays (with many zero elements), negative elements, and duplicate elements. The implementation should only use basic array manipulation operations, without relying on any built-in functions or libraries.
"""

def transpose(matrix):
    n = len(matrix)
    m = len(matrix[0])
    transposed = [[0] * n for _ in range(m)]
    
    for i in range(n):
        for j in range(m):
            transposed[j][i] = matrix[i][j]
    
    return transposed