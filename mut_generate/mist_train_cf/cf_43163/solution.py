"""
QUESTION:
Implement a function `is_magic_square(matrix: List[List[int]]) -> bool` that checks if a given square matrix is a magic square or not. The function takes a 2D list `matrix` as input, where each inner list represents a row of the matrix, containing only positive integers. The function should return `True` if the given matrix is a magic square (i.e., the sum of each row, each column, and both main diagonals are the same), and `False` otherwise. The input matrix will have at least 1 row and 1 column.
"""

from typing import List

def is_magic_square(matrix: List[List[int]]) -> bool:
    n = len(matrix)
    target_sum = sum(matrix[0])  

    for row in matrix:
        if sum(row) != target_sum:
            return False

    for j in range(n):
        col_sum = sum(matrix[i][j] for i in range(n))
        if col_sum != target_sum:
            return False

    if sum(matrix[i][i] for i in range(n)) != target_sum:
        return False

    if sum(matrix[i][n - 1 - i] for i in range(n)) != target_sum:
        return False

    return True