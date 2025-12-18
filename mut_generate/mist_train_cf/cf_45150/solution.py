"""
QUESTION:
Write a function `is_exponent_of_two` that determines whether a given positive integer is a power of 2. The function should return `True` if the number is a power of 2 and `False` otherwise. The input is a positive integer.
"""

def is_exponent_of_two(num):
    while num > 1:
        if num % 2 != 0:
            return False
        num = num / 2
    return True