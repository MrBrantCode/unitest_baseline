"""
QUESTION:
Write a function `filter_numeric_strings` that takes a list of strings as input and returns a new list containing only the numeric strings of length 1. The function should return an empty list if the input list is empty or contains no numeric strings of length 1.
"""

from typing import List

def filter_numeric_strings(input_list: List[str]) -> List[str]:
    return [s for s in input_list if s.isdigit() and len(s) == 1]