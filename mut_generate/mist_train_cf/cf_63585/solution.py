"""
QUESTION:
Construct a function `smallest_triangular_num(n)` that computes the position of the smallest triangular number with `n` digits. The function should accept a positive integer `n` (or a list of positive integers) as input, where `n` is the desired number of digits in the triangular number. The function should return the smallest triangular number and its corresponding position, either as a tuple for a single input or a list of tuples for multiple inputs.

The function should efficiently handle large inputs (up to 10^12), round non-integer inputs to the nearest integer, and return an error message for invalid inputs (non-positive integers or non-integer inputs). Additionally, the function should utilize caching to avoid recomputing previously calculated values.
"""

import math

CACHE = {}
def smallest_triangular_num(n):
    if not isinstance(n, int) or n <= 0:
        return "Error: Input should be a positive integer"
    
    if n in CACHE:
        return CACHE[n]

    left, right = n, 10**12
    while left < right:
        mid = (left + right) // 2
        triangular_num = mid * (mid + 1) // 2
        num_of_digits = math.floor(math.log10(triangular_num)) + 1

        if num_of_digits == n:
            CACHE[n] = (triangular_num, mid)
            return (triangular_num, mid)
        elif num_of_digits < n:
            left = mid + 1
        else:
            right = mid

    CACHE[n] = (triangular_num, mid)
    return (triangular_num, mid)