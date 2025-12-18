"""
QUESTION:
Create a function called `intersperse` that takes a list of integers `numbers`, an integer `delimeter`, and an optional boolean parameter `even_positions_only` (default to False). The function should return a list where the integer `delimeter` is inserted between every two consecutive elements of `numbers`. If `even_positions_only` is True, the `delimeter` should only be inserted between consecutive elements at even indexes.
"""

from typing import List

def intersperse(numbers: List[int], delimeter: int, even_positions_only: bool = False) -> List[int]:
    if even_positions_only:
        for i in range(2, len(numbers), 2):
            numbers.insert(i, delimeter)
    else:
        for i in range(len(numbers)-1, 0, -1):
            numbers.insert(i, delimeter)
    return numbers