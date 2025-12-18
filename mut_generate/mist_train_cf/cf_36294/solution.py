"""
QUESTION:
Implement a function `sum_positive_abs` that takes a list of integers as input and returns the sum of the absolute values of the positive numbers in the list, ignoring any negative numbers and zeros. The function should return an integer value.
"""

from typing import List

def sum_positive_abs(numbers: List[int]) -> int:
    total_sum = 0
    for num in numbers:
        if num > 0:
            total_sum += num
        elif num == 0:
            continue
        else:
            continue
    return total_sum