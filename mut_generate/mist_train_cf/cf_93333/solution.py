"""
QUESTION:
Write a function `check_power(n)` to determine if a given number `n` can be expressed as the power of some other number, i.e., if there exist integers `a` and `b` (where `a > 1` and `b > 1`) such that `a^b = n`. The function should return `True` if such integers exist, and `False` otherwise.
"""

import math

def check_power(n):
    if n <= 1:
        return False
    
    # Check for all possible values of 'a' from 2 to sqrt(n)
    for a in range(2, int(math.sqrt(n)) + 1):
        b = math.log(n, a)
        # Check if 'b' is an integer and a^b is equal to n
        if b.is_integer() and a**int(b) == n:
            return True
    
    return False