"""
QUESTION:
Implement a function `transpose(matrix, n, m)` that prints the transpose of a given matrix without using any built-in functions, libraries, or additional data structures. The function should take the matrix and its dimensions `n` and `m` as inputs and should have a time complexity of O(N*M). The function should be implemented recursively.

Note: The matrix can contain integers, decimals, or characters.
"""

def transpose(matrix, n, m):
    # Base case: if the matrix is empty, return
    if n == 0 or m == 0:
        return
    
    # Print the first column of the matrix
    for i in range(n):
        print(matrix[i][0], end=' ')
    print()
    
    # Recursive call on the submatrix excluding the first column
    transpose(matrix, n, m-1)