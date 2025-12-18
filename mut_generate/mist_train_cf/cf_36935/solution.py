"""
QUESTION:
Write a function `sparse_to_dense(i, j, val, n, m)` to convert sparse matrix representations into a 2D matrix representation. The function should take five parameters:
- `i` is a list of integers representing the row indices of the sparse matrix.
- `j` is a list of integers representing the column indices of the sparse matrix.
- `val` is a list of integers representing the values of the sparse matrix.
- `n` is an integer representing the number of rows in the dense matrix.
- `m` is an integer representing the number of columns in the dense matrix.
The function should return a 2D list representing the dense matrix.
"""

from typing import List

def sparse_to_dense(i: List[int], j: List[int], val: List[int], n: int, m: int) -> List[List[int]]:
    dense_matrix = [[0 for _ in range(m)] for _ in range(n)]
    for idx in range(len(i)):
        dense_matrix[i[idx]][j[idx]] = val[idx]
    return dense_matrix