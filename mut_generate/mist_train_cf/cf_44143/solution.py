"""
QUESTION:
Write a function `maxEqualRowsAfterFlips(matrix)` that determines and returns the maximum number of rows that can be made identical in value after flipping a certain number of columns in the given binary matrix `matrix`. The function takes a 2D list `matrix` of dimensions `m x n` as input, where `m` and `n` are both greater than or equal to 1 and less than or equal to 300, and the values of `matrix[i][j]` are either 0 or 1.
"""

from collections import Counter

def maxEqualRowsAfterFlips(matrix):
    count = Counter()
    for row in matrix:
        unit = min(row.count(0), row.count(1))
        count[tuple(i ^ unit for i in row)] += 1
    return max(count.values())