"""
QUESTION:
Write a function called `flip_along_diagonal` that takes a square matrix as input and returns the matrix flipped along its diagonal. The function should work for square matrices of any size.
"""

def flip_along_diagonal(mat):
    return [[mat[j][i] for j in range(len(mat))] for i in range(len(mat[0]))]