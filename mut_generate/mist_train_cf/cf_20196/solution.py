"""
QUESTION:
Create a function named `transpose_array` that takes a 2-dimensional array as input and returns its transpose. The transpose of a matrix is obtained by switching the row and column indices of each element. The function must not use any built-in functions or libraries to transpose the array, and it must have a time complexity of less than O(n * m) and a space complexity of less than O(n * m), where n is the number of rows and m is the number of columns in the input array.
"""

def transpose_array(matrix):
    n = len(matrix)
    m = len(matrix[0])
    
    transposed = [[0 for _ in range(n)] for _ in range(m)]
    
    for i in range(n):
        for j in range(m):
            transposed[j][i] = matrix[i][j]
    
    return transposed