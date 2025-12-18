"""
QUESTION:
Given a non-negative integer `rowIndex`, write a function `getPascalRow(rowIndex)` to generate the `rowIndex`-th row of Pascal's triangle as a list. The row index starts from 0 and the elements of the row are 0-indexed. The function should return a list of integers representing the `rowIndex`-th row.
"""

from typing import List

def getPascalRow(rowIndex: int) -> List[int]:
    if rowIndex == 0:
        return [1]
    row = [1]
    for i in range(1, rowIndex + 1):
        next_val = row[i - 1] * (rowIndex - i + 1) // i
        row.append(next_val)
    return row