"""
QUESTION:
Create a recursive function `swap_numbers(a, b)` that swaps the values of two given numbers `a` and `b` without using a temporary variable. The function should return the swapped values of `a` and `b`.
"""

def entrance(a, b):
    if a == b:
        return a, b
    else:
        a = a + b
        b = a - b
        a = a - b
        return a, b