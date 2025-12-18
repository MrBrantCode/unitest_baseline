"""
QUESTION:
Write a function called `is_power_of_three` that takes an integer `n` as input and returns `True` if `n` is a power of three, and `False` otherwise. The function should handle integers of all ranges, including negative numbers and zero.
"""

def is_power_of_three(n: int) -> bool:
    if n <= 0:
        return False
    while n % 3 == 0:
        n /= 3
    return n == 1