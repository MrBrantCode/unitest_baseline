"""
QUESTION:
Implement a function `modify_matrix` that takes a square matrix `A` and two lists, `diagonals` and `values`, as input. The function should modify the matrix `A` by filling the specified diagonals with the given values. The `diagonals` list contains tuples representing the starting and ending indices of the diagonals to be modified, and the `values` list contains the corresponding values to be filled in the diagonals. The function should return the modified matrix.
"""

from typing import List, Tuple

def modify_matrix(A: List[List[int]], diagonals: List[Tuple[int, int]], values: List[int]) -> List[List[int]]:
    for i in range(len(diagonals)):
        start, end = diagonals[i]
        value = values[i]
        for j in range(start, end+1):
            A[j][j] = value
    return A