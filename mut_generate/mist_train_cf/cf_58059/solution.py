"""
QUESTION:
Create a function `generate_matrix` to create a matrix of size `m x n` filled with a specified value. The function should take two or three parameters: the number of rows `m`, the number of columns `n`, and an optional value to fill the matrix (default is 0).
"""

def generate_matrix(m, n, value=0):
    return [[value]*n for _ in range(m)]