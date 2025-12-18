"""
QUESTION:
Write a function `maxCount` that takes in three parameters: `m` and `n` representing the dimensions of an m x n matrix initialized with all 0's, and `ops` which is a list of operations where each operation is a list of two integers [a, b] representing the number of rows and columns to increment by 1. Return the number of maximum integers in the resulting matrix after performing all operations. The function should handle the case where `ops` is empty, returning the total number of elements in the matrix.
"""

from typing import List

def maxCount(m: int, n: int, ops: List[List[int]]) -> int:
    min_row = m
    min_col = n
    for op in ops:
        min_row = min(min_row, op[0])
        min_col = min(min_col, op[1])
    return min_row * min_col if ops else m * n