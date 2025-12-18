"""
QUESTION:
Implement a function named `calculate_sum` that takes a list of integers and returns their sum. The function should utilize a custom reduce functionality without using any loops, the built-in `sum()` function, or importing the `reduce()` function from the `functools` module. The input list will contain at least one integer.
"""

from typing import List

def calculate_sum(numbers: List[int]) -> int:
    def custom_reduce(function, sequence):
        it = iter(sequence)
        result = next(it)
        for element in it:
            result = function(result, element)
        return result
    
    return custom_reduce(lambda x, y: x + y, numbers)