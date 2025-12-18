"""
QUESTION:
Create a function `intersperse` that takes a list of integers `numbers` and an integer `delimiter` as input. If `delimiter` is non-negative, the function should return a new list where `delimiter` is inserted between every pair of adjacent elements in `numbers`. If `delimiter` is negative, the function should return a new list where each element in `numbers` is multiplied by the absolute value of `delimiter`.
"""

from typing import List

def intersperse(numbers: List[int], delimiter: int) -> List[int]:
    """
    This function injects 'delimiter' into the 'numbers' array, between each pair of adjacent elements, 
    and properly handles situations when 'delimiter' is negative.
    """
    new_numbers = []
    if delimiter < 0:
        for number in numbers:
            new_numbers.append(number * abs(delimiter))
    else:
        for i in range(len(numbers)):
            new_numbers.append(numbers[i])
            if i != len(numbers) - 1:
                new_numbers.append(delimiter)

    return new_numbers