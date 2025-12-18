"""
QUESTION:
Develop a function called `intersperse` that accepts a list `numbers` containing integers and a singular integer `delimeter`. The function should produce a list which consists of the integer `delimeter` positioned among every pair of consecutive numbers in the `numbers` list. If the `delimeter` is negative, use its absolute value as the index(es) to exclude from the positioning of the `delimeter`. The function should return the modified list of integers.
"""

from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    # Manage negative delimeter
    if delimeter < 0:
        return numbers
    
    result = []
    # Only integrate the delimeter if it is nonnegative
    for num in numbers[:-1]:
        result.append(num)
        result.append(delimeter)
    
    # Remember to append the last number
    if numbers:
        result.append(numbers[-1])
    
    return result