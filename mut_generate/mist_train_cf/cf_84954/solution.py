"""
QUESTION:
Write a function called `calculate_remainder` that takes two parameters, `base` and `exponent`, and returns the remainder when `base` raised to the power of `exponent` is divided by 4. The function should be able to handle large numbers, taking into consideration potential precision issues or out-of-range errors.
"""

def calculate_remainder(base, exponent):
    return (base ** exponent) % 4