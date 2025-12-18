"""
QUESTION:
Write a function named `is_perfect_square` that takes an integer `n` as input and returns a tuple. If `n` is a perfect square, the tuple should contain `True` and the square root of `n` rounded to 3 decimal places. If `n` is not a perfect square, the tuple should contain `False` and `-1`. The function should handle very large integers efficiently.
"""

import math

def is_perfect_square(n):
    if n < 0:  
        return False, -1

    root = math.sqrt(n)
    if int(root + 0.5) ** 2 == n:  
        return True, round(root,3)
    else:
        return False, -1