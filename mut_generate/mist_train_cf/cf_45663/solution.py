"""
QUESTION:
Write a function called `is_power_of_three` that determines whether a given integer is a power of three or not, and returns `True` if it is, and `False` otherwise. The input will always be a positive integer.
"""

def is_power_of_three(n):
    if n <= 0:
        return False
    while n % 3 == 0:
        n /= 3
    return n == 1