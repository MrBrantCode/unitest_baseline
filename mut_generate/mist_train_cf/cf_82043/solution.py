"""
QUESTION:
Write a Python function named `intersperse` that accepts a list of integers `numbers` and an integer `delimiter`. The function should return a new list where a `delimiter` is placed between every pair of consecutive elements in the `numbers` list.
"""

from typing import List

def intersperse(numbers: List[int], delimiter: int) -> List[int]:
    if len(numbers) == 0:
        return []
    
    result = []
    
    for num in numbers[:-1]:
        result.append(num)
        result.append(delimiter)

    result.append(numbers[-1])
    
    return result