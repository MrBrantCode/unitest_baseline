"""
QUESTION:
Create a function named `tuple_to_complex` that takes a tuple of two floats as input and returns a complex number. The function should use type hinting for both the argument and the return value, following Python's best practices.
"""

from typing import Tuple

def tuple_to_complex(numbers: Tuple[float, float]) -> complex:
    return complex(numbers[0], numbers[1])