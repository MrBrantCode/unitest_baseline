"""
QUESTION:
Create a function `peculiar_function` that takes a tuple of two floating-point numbers as input and returns a complex number. The function should use the cmath library and return a complex number with non-integer real and imaginary parts.
"""

from typing import Tuple
import cmath

def peculiar_function(input_tuple: Tuple[float, float]) -> complex:
    x, y = input_tuple
    result = cmath.exp(x) / cmath.cos(y)
    return result