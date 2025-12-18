"""
QUESTION:
Write a function `check_matrix_multiplication_compatibility` that takes four integers `m`, `n`, `p`, and `q` representing the dimensions of two matrices as input, where the first matrix has dimensions `m x n` and the second matrix has dimensions `p x q`. The function should return `True` if the shapes are compatible for matrix multiplication (i.e., `n` equals `p`) and `False` otherwise.
"""

def check_matrix_multiplication_compatibility(m, n, p, q):
    return n == p