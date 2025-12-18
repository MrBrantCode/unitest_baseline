"""
QUESTION:
Write a function `count_zeros` that takes a 2D list of integers `matrix` and an optional boolean parameter `strict_zero` (defaulting to `False`) as input. The function should return the count of zeros in the matrix. If `strict_zero` is `True`, only count exact integer zeros. If `strict_zero` is `False`, also count values that equate to `False` in a boolean context, including empty strings, string zeros, and boolean `False`.
"""

from typing import List, Any

def count_zeros(matrix: List[List[Any]], strict_zero: bool = False) -> int:
    zero_count = 0
    for row in matrix:
        for num in row:
            if strict_zero:
                if num == 0:
                    zero_count += 1
            else:
                if not num:
                    zero_count += 1
    return zero_count