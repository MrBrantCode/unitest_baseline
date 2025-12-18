"""
QUESTION:
Write a function `intersperse` that takes a list of integers `numbers` and a single integer `delimeter`. The function should return a list containing the integer `delimeter` situated between each pair of consecutive elements from the `numbers` list. If the `delimeter` is negative, return the original `numbers` list without modifications.
"""

from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    result = []
    if delimeter < 0:
        return numbers
    if numbers:
        result.append(numbers[0])
        for num in numbers[1:]:
            result.append(delimeter)
            result.append(num)
    return result