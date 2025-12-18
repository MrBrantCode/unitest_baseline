"""
QUESTION:
Create a function called `power` that raises a given decimal number `x` to the `n`th power, where `n` can be a negative number. The function should ensure that `x` is within a specified range (`min_range` to `max_range`) and return an error message if it is not. Additionally, if `n` is not an integer, the function should round it to the nearest integer. The function should achieve a time complexity of O(log N) or better.
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