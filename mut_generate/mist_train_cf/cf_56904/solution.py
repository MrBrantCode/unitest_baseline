"""
QUESTION:
Create a function `is_perfect_square(num)` that checks whether the input number is a perfect square. The function should return `True` if the number is a perfect square, `False` otherwise. Additionally, the function should return a message 'Input should be a positive integer' if the input number is not a positive integer. The function should handle non-integer and negative values without throwing exceptions and should have a time complexity of O(1).
"""

import math

def is_perfect_square(num):
    if not isinstance(num, int) or num < 0:
        return 'Input should be a positive integer'
    elif math.isqrt(num)**2 == num:
        return True
    else:
        return False