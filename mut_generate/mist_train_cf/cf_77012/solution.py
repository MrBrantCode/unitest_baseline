"""
QUESTION:
Create a function `multiply_matrices(A, B)` that takes two matrices `A` and `B` as input and returns their product. The function should work for any two matrices that can be multiplied, i.e., the number of columns in `A` is equal to the number of rows in `B`. The input matrices are represented as lists of lists, where each inner list represents a row in the matrix. The output should also be a list of lists representing the product matrix.
"""

def multiply_matrices(A, B):
    return [[sum(a*b for a, b in zip(A_row, B_col)) for B_col in zip(*B)] for A_row in A]