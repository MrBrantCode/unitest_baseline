"""
QUESTION:
Write a function named `transpose` that takes a sparse matrix `mat` of size `m x n` and returns the transposed matrix `matT` of size `n x m`. The input matrix `mat` is a 2D list where `m == mat.length` and `n == mat[i].length`, and all elements in the matrix are integers within the range `-100 <= mat[i][j] <= 100`. The function should have a time complexity that can handle `1 <= m, n <= 100`.
"""

def transpose(mat):
    return [[mat[j][i] for j in range(len(mat))] for i in range(len(mat[0]))]