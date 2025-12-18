"""
QUESTION:
Write a function `intersperse` that accepts a list of integers `numbers` and a separate integer `delimeter`. The function should construct a new list by inserting `delimeter` in between every pair of adjacent elements in `numbers`. If `delimeter` is negative, use its absolute value. Ensure that `delimeter` is not appended at the end of the resulting list.
"""

from typing import List

def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """ The function should install 'delimeter' between each pair of adjacent elements in the 'numbers' array, and handle negative 'delimeter' situations properly. 
    """
    
    #   Handling negative 'delimeter' situation
    if delimeter < 0:
        delimeter = abs(delimeter)

    result = []
    for num in numbers:
        result += [num, delimeter]
    
    # Removing the last unnecessary 'delimeter'
    result = result[:-1] 
    
    return result