"""
QUESTION:
Write a function `sum_of_sq_root(arr)` that calculates the sum of the square roots of unique positive integers in an array. The function should return `None` if the array is empty, and 0 if the array does not contain any non-zero, non-negative numbers. The function should ignore non-integer and hexadecimal numbers in the array.
"""

import math
def sum_of_sq_root(arr):
    if not arr:
        return None
    
    unique_numbers = set([x for x in arr if isinstance(x, int) and x > 0])
    
    sum_sq_roots = sum([math.sqrt(num) for num in unique_numbers])
    
    return sum_sq_roots