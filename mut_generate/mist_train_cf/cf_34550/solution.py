"""
QUESTION:
Implement a function `count_unique_elements` that takes a list of integers as input and returns the count of unique elements in the list, where a unique element is defined as an element that appears only once in the list. Do not use any built-in Python functions that directly solve this problem.
"""

from typing import List

def count_unique_elements(arr: List[int]) -> int:
    unique_elements = set()
    repeated_elements = set()
    
    for num in arr:
        if num in unique_elements:
            unique_elements.remove(num)
            repeated_elements.add(num)
        elif num not in repeated_elements:
            unique_elements.add(num)
    
    return len(unique_elements)