"""
QUESTION:
Write a function `add_and_display_binary` that takes two integers `a` and `b` as input and returns their sum in binary format. The function should not take any other parameters.
"""

def add_and_display_binary(a, b):
    """Return the sum of two integers in binary format."""
    return bin(a + b)[2:]