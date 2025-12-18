"""
QUESTION:
Write a function `matrix_modes(matrix)` that takes a 2D matrix as input where each cell contains a list of integers, and returns a 2D list where each cell contains a list of mode(s) for the corresponding cell in the input matrix. If there are multiple modes in a series, return all of them. The function should have an optimized time complexity.
"""

from collections import Counter

def matrix_modes(matrix):
    return [[sorted(k for k,v in Counter(row[j]).most_common() if v == max(Counter(row[j]).values())) for j in range(len(row))] for row in matrix]