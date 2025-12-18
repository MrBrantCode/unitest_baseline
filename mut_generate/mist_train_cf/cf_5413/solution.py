"""
QUESTION:
Write a function `transpose` that takes a matrix `matrix` and its dimensions `n` and `m` as inputs, where `n` is the number of rows and `m` is the number of columns. The function should print the transpose of the matrix, with a time complexity of O(N*M), without using any built-in functions or libraries for transposing the matrix, or any additional data structures or matrices. The function should be implemented recursively.
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