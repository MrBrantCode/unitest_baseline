"""
QUESTION:
Create a function named `rotateMatrix` that takes a square matrix `mat` and an integer `N` as input, and returns the matrix rotated 90 degrees to the right `N` times. The function should work with square matrices of any dimension, and `N` can be any integer, including negative numbers.
"""

def rotateMatrix(mat, N):
    # Transpose the matrix
    for x in range(0, len(mat)):
        for y in range(x, len(mat)):
            temp = mat[x][y]
            mat[x][y] = mat[y][x]
            mat[y][x] = temp

    # Swap columns moving inwards from outwards
    for x in range(0, len(mat)):
        for y in range(0, int(len(mat) / 2)):
            temp = mat[x][y]
            mat[x][y] = mat[x][len(mat) - y - 1]
            mat[x][len(mat) - y - 1] = temp

    # If N is more than 1, call the function recursively
    if N > 1:
        rotateMatrix(mat, N - 1)

    return mat