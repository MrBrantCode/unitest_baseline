"""
QUESTION:
Implement the function `extract_integer(number: float, round_down: bool = True) -> int` to return the integer part of the given floating point number, considering the specified rounding type. The function should handle both positive and negative numbers. If `round_down` is `True`, round down to the nearest integer, otherwise round up.
"""

import math

def extract_integer(number: float, round_down: bool = True) -> int:
    if round_down:
        return math.floor(number)
    else:
        return math.ceil(number)