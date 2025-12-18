"""
QUESTION:
Write a Python function `intersperse` that takes a list of integers `numbers` and an integer `delimiter`. The function should insert `delimiter` between each pair of consecutive elements in `numbers` and return the resulting list. If `delimiter` is negative, the function should skip its absolute value's number of elements from the start of `numbers`.
"""

from typing import List

def intersperse(numbers: List[int], delimiter: int) -> List[int]:
    """ Inserts the integer 'delimiter' between each pair of adjacent elements. 
        If 'delimiter' is negative, it skips its absolute value's number of 
        elements from the beginning.
    """
    result = []
    if numbers:
        if delimiter < 0:
            # Skip abs(delimiter) elements from the beginning
            start_index = abs(delimiter)
            numbers = numbers[start_index:]

        for num in numbers:
            result.append(num)
            result.append(delimiter)

        result.pop()  # Remove last delimiter
    return result