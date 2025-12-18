"""
QUESTION:
Implement a function `is_power_of_two` that takes an integer `n` as input and returns `True` if the number is a power of two, and `False` otherwise.
"""

def is_power_of_two(n):
    if n <= 0:
        return False
    return (n & (n - 1)) == 0