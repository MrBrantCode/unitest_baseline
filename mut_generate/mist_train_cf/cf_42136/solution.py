"""
QUESTION:
Create a function named `is_divisible_by_all` that determines whether a given positive integer `num` is divisible by all numbers in a specified range from `start` to `end` (inclusive). The function should return `True` if `num` is divisible by all numbers in the range, and `False` otherwise.
"""

def is_divisible_by_all(num, start, end):
    for i in range(start, end + 1):
        if num % i != 0:
            return False
    return True