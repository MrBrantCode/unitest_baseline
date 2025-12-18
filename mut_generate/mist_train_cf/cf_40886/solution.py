"""
QUESTION:
Implement a function `generate_pascals_triangle(num_rows)` that takes an integer `num_rows` as input and returns Pascal's triangle as a 2D list of integers, where each inner list represents a row in the triangle. The function should return the triangle up to the given number of rows. The input `num_rows` is a non-negative integer.
"""

from typing import List

def generate_pascals_triangle(num_rows: int) -> List[List[int]]:
    result = []
    for i in range(num_rows):
        temp = [1]
        if i > 0:
            for j in range(1, i):
                temp.append(result[-1][j-1] + result[-1][j])
            temp.append(1)
        result.append(temp)
    return result