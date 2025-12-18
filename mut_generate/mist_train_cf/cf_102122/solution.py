"""
QUESTION:
Create a function `add_two_numbers` that takes two integer arguments and returns their sum. The function should handle cases where the input arguments are not integers, returning an error message. It should also handle negative integers as input, and only use basic arithmetic operations.
"""

def add_two_numbers(a, b):
    if not isinstance(a, int) or not isinstance(b, int):
        return "Error: Both inputs must be integers"
    sum = a + b
    return sum