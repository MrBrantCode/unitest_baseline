"""
QUESTION:
Given a 2D matrix `mat` of integers, where each row is sorted in non-decreasing order, write a function `smallestCommonElement` to find the smallest common element in all rows of the matrix. If there is no common element, return -1. The function should take `mat` as input and return an integer.
"""

from typing import List
from bisect import bisect_left

def smallestCommonElement(mat: List[List[int]]) -> int:
    if not mat:
        return -1

    values = mat[0]
    for row in mat[1:]:
        common_values = []
        i, j = 0, 0
        while i < len(values) and j < len(row):
            if values[i] == row[j]:
                common_values.append(values[i])
                i += 1
                j += 1
            elif values[i] < row[j]:
                i += 1
            else:
                j += 1
        values = common_values

    return values[0] if values else -1