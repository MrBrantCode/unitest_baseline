"""
QUESTION:
Implement a function `is_power_of_three` that takes an integer `n` as input and returns `True` if `n` is a power of three, and `False` otherwise.
"""

def is_power_of_three(n):
    if n <= 0:
        return False
    while n % 3 == 0:
        n /= 3
    return n == 1