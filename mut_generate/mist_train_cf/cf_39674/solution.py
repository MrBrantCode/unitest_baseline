"""
QUESTION:
Implement the `max_digits_count` function that takes a list of integers as input and returns the maximum number of digits present in any of the integers in the list. The function should handle both positive and negative integers, and the input list can contain any number of integers. The function must return a non-negative integer value.
"""

from typing import List

def max_digits_count(numbers: List[int]) -> int:
    max_digits = 0
    for num in numbers:
        num_digits = len(str(abs(num)))
        if num_digits > max_digits:
            max_digits = num_digits
    return max_digits