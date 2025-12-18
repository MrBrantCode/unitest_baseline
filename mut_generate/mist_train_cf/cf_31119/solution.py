"""
QUESTION:
Write a function called `calculate_square_root` that takes a list of numbers and two constant values `c` and `h` as input. The function should calculate the square root of each number using the formula `round(sqrt(2 * c * number / h))`, convert the results to strings, and return them as a comma-separated string.
"""

import math

def calculate_square_root(items, c, h):
    value = []
    for d in items:
        result = int(round(math.sqrt(2 * c * float(d) / h)))
        value.append(str(result))
    return ','.join(value)