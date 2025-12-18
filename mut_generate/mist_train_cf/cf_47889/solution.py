"""
QUESTION:
Create a function `intersperse` that takes a list of integers and a separate integer `delimiter` as input. The function should return a new list where the absolute value of the `delimiter` is placed between every pair of integers from the initial list. If the input list is empty, the function should return an empty list.
"""

from typing import List

def intersperse(numbers: List[int], delimiter: int) -> List[int]:
    """Custom Python function with increased difficulty"""
    
    # Check if list is empty
    if not numbers:
        return []
    
    # If delimiter is negative, consider its absolute value
    delimiter = abs(delimiter)

    # Create a new list with the delimiter interspersed between each pair of numbers
    new_list = [numbers[0]]
    for num in numbers[1:]:
        new_list.extend([delimiter, num])
        
    return new_list