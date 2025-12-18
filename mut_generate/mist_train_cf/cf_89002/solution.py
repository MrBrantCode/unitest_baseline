"""
QUESTION:
Create a function `transpose(matrix)` that takes a 2-dimensional array of size n x m as input and returns its transpose. The function should be able to handle arrays of any size, with non-integer elements, sparse arrays, negative elements, and duplicate elements. It should not use any built-in functions or libraries to transpose the array.
"""

def transpose(matrix):
    n = len(matrix)
    m = len(matrix[0])
    transposed = [[0] * n for _ in range(m)]
    
    for i in range(n):
        for j in range(m):
            transposed[j][i] = matrix[i][j]
    
    return transposed