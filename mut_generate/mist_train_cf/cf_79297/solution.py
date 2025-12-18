"""
QUESTION:
You are given a binary matrix `matrix` of dimensions `m x n`. You are permitted to select any quantity of columns within the matrix and invert every cell within the chosen column(s). Determine and return the maximum count of rows that possess identical values following a certain number of inversions.

Constraints:
`m == matrix.length`
`n == matrix[i].length`
`1 <= m, n <= 300`
`matrix[i][j]` is either `0` or `1`.

Implement the function `maxEqualRowsAfterFlips(matrix: List[List[int]]) -> int` to solve the problem.
"""

from typing import List
from collections import Counter

def maxEqualRowsAfterFlips(matrix: List[List[int]]) -> int:
   # convert rows to a binary number representation
    binaries = [''.join(map(str, row)) for row in matrix]
    # flip 1s to 0s and 0s to 1s for each binary representation
    flipped = [''.join('1' if c == '0' else '0' for c in bin_rep) for bin_rep in binaries]
    # count the frequency of each binary and flipped representation
    count = Counter(binaries + flipped)
    # the answer is the max frequency
    return max(count.values())