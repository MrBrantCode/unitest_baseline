"""
QUESTION:
Design a function `find_pairs(matrix, target)` that takes a multidimensional matrix and a target number as input, and returns the indices of two numbers in the matrix whose sum equals the target number. The numbers can be located at distinct indices in any direction (horizontal, vertical, diagonal, or anti-diagonal). The function should handle edge cases where no valid solution exists. The matrix can have repeated values and the target number can range from 0 to 200.
"""

def find_pairs(matrix, target):
    rows, cols = len(matrix), len(matrix[0])
    partial = {}
    for i in range(rows):
        for j in range(cols):
            remaining = target - matrix[i][j]
            if remaining in partial:
                return partial[remaining],(i,j)
            partial[matrix[i][j]] = (i,j)
    return -1