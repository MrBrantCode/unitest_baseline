"""
QUESTION:
Write a function `generate_pascals_triangle_row(n: int)` that generates the nth row of Pascal's Triangle as a list of integers, where each number is the sum of the two directly above it in the previous row, and optimize the algorithm to use only O(k) extra space, where k is the number of elements in the output row.
"""

from typing import List

def entrance(n: int) -> List[int]:
    row = [1] * (n + 1)
    for i in range(2, n + 1):
        for j in range(i - 1, 0, -1):
            row[j] += row[j - 1]
    return row