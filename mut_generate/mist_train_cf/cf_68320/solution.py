"""
QUESTION:
Construct an `intersperse` function that takes a list of integers (`numbers`) and an individual integer (`delimeter`). The function should return a list with the `delimeter` situated between sequential elements in the `numbers` array. If the `delimeter` is negative, the function should return the original `numbers` list without any modifications.
"""

from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    if delimeter < 0:
        return numbers
    result = []
    for i, num in enumerate(numbers):
        result.append(num)
        if i < len(numbers) - 1:
            result.append(delimeter)
    return result