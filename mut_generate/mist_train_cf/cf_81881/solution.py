"""
QUESTION:
Write a function named `filter_integers` that takes a list of arbitrary elements as input and returns a new list containing only the integer elements from the original list. The function should exclude non-integer numeric types, such as floats.
"""

from typing import List, Any

def filter_integers(values: List[Any]) -> List[int]:
    """Filter the provided collection of arbitrary Python elements solely for integer data types"""
    return [value for value in values if type(value) == int]