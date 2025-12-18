"""
QUESTION:
Construct a function `construct_square(n)` that takes an integer parameter `n` and returns an nxn square matrix filled with successive positive integers from 1 to `n^2` in row-major order.
"""

def construct_square(n):
    matrix = [[0]*n for _ in range(n)]
    num = 1
    for i in range(n):
        for j in range(n):
            matrix[i][j] = num
            num += 1
    return matrix