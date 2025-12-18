"""
QUESTION:
Create a function `power` that raises a given decimal number `x` to the `n`th power, where `n` can be a negative number or a non-integer that will be rounded to the nearest integer. The function must ensure `x` is within a specific range defined by `min_range` and `max_range` (inclusive), returning an error message if it's not. The function should achieve this with a time complexity of O(log N) or better.
"""

import math

def power(x, n, min_range, max_range):
    if x < min_range or x > max_range:
        return "Error: Number out of range"
    
    if not isinstance(n, int):
        n = round(n)
    
    result = recursive_power(x, abs(n))
    
    if n < 0:
        return 1 / result
    
    return result

def recursive_power(x, n):
    if n == 0:
        return 1
    
    if n % 2 == 0:
        half_power = recursive_power(x, n // 2)
        return half_power * half_power
    
    return x * recursive_power(x, n - 1)