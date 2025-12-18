"""
QUESTION:
Write a function named `reverse_matrix` that takes a 2D list (matrix) as input and returns the modified matrix with the first and last elements of each row swapped, and the remaining elements in each row reversed. The function should also check if the input matrix is square (i.e., all rows have the same number of elements as the number of rows) and return "Matrix is not square!" if it's not. Do not use any built-in reverse function.
"""

def reverse_matrix(mat):
    # Check if the matrix is square
    if len(set(map(len, mat))) != 1 or len(mat) != len(mat[0]):
        return "Matrix is not square!"

    for i in range(len(mat)):
        mat[i][0], mat[i][-1] = mat[i][-1], mat[i][0]
        for j in range(1, len(mat[i])//2):
            mat[i][j], mat[i][-(j+1)] = mat[i][-(j+1)], mat[i][j]

    return mat