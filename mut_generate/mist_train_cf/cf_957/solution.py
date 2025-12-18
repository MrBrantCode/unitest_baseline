"""
QUESTION:
Implement the `add_matrices` function, which takes two matrices `a` and `b` as input, each represented as a list of lists of integers, and returns a new matrix that is the sum of `a` and `b`. The number of rows in `a` and `b` will be equal, and the number of elements in each row of `a` and `b` will also be equal. The function should handle matrices with up to 10^3 rows and columns.
"""

from typing import List

def add_matrices(a: List[List[int]], b: List[List[int]]) -> List[List[int]]:
    rows = len(a)
    cols = len(a[0])
    result = [[0] * cols for _ in range(rows)]
    for i in range(rows):
        for j in range(cols):
            result[i][j] = a[i][j] + b[i][j]
    return result