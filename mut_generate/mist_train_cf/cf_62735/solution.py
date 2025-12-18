"""
QUESTION:
Create a function called `intersperse` that takes a list of integers `numbers` and an integer `delimeter`. It should return a new list where the `delimeter` is inserted between every two consecutive elements from the list `numbers`. The function should handle the case when `numbers` is an empty list and return an empty list in that case.
"""

from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    result = []
    for num in numbers:
        result.append(num)
        result.append(delimeter)
    return result[:-1] if result else result