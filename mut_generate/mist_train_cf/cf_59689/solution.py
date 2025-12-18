"""
QUESTION:
Implement the function `intersperse` that takes in a list of integers `numbers` and an integer `delimeter`. The function should return a new list where `delimeter` is inserted between the elements of `numbers`. If `delimeter` is negative, its absolute value is used as the number of elements to bypass before inserting the `delimeter`. For example, if `delimeter` is -2, it means to insert `delimeter` after every 3 elements (2 elements bypassed). The function should handle edge cases such as an empty `numbers` list or a `delimeter` of 0.
"""

from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    result = []
    if delimeter >= 0:  
        for i, num in enumerate(numbers):
            result.append(num)
            if i < len(numbers) - 1:
                result.append(delimeter)
    else:  
        bypass_count = abs(delimeter)
        for i, num in enumerate(numbers):
            result.append(num)
            if (i + 1) % (bypass_count + 1) == 0 and i < len(numbers) - 1:
                result.append(-delimeter)
    return result