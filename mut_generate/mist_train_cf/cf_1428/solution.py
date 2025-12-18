"""
QUESTION:
Create a function `create_array` that takes three integers `rows`, `columns`, and `value`, and returns a 2D array of size `rows` x `columns`. Each element in the array should be the product of its row index, column index, and `value`. The function should assume that `rows` and `columns` are greater than or equal to 1, and that the given `value` is an integer.
"""

from typing import List

def create_array(rows: int, columns: int, value: int) -> List[List[int]]:
    return [[value * (i * columns + j) for j in range(columns)] for i in range(rows)]