"""
QUESTION:
Create a function called `intersperse` that takes a list of integers `numbers` and an integer `delimeter`. The function should return a new list where `delimeter` is inserted between each pair of adjacent elements in `numbers`. If `delimeter` is negative, the function should return the original list `numbers` without any modifications.
"""

from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """
    Install the digit 'delimeter' among each pair of adjacent elements present in the input array `numbers', 
    while addressing negative delimeter instances.
    """
    if delimeter < 0:
        return numbers
    
    result = []
    for num in numbers:
        result.append(num)
        result.append(delimeter)
    
    # If the list is not empty, remove the last appended delimeter
    if result:
        result.pop()
    
    return result