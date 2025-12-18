"""
QUESTION:
Design a function `advanced_base_translation_avg(n, m, base)` that calculates the arithmetic mean of all integers between `n` and `m` (inclusive), rounds up to the nearest integer, and converts the result to a base between 2 and 10 (inclusive). If `m` is less than `n` or `base` is outside the range 2-10, return -1.
"""

import math

def advanced_base_translation_avg(n, m, base):
    if m < n or base < 2 or base > 10: 
        return -1
    
    avg = math.ceil(sum(range(n, m+1)) / (m-n+1))
    
    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    converted = ""
    while avg > 0:
        avg, idx = divmod(avg, base)
        converted = digits[idx] + converted
    return converted