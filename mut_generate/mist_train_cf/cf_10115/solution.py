"""
QUESTION:
Create a function `is_prime(num)` that determines whether a given integer `num` is a prime number or not without using any built-in functions or libraries. The function should return `True` if `num` is prime and `False` otherwise.
"""

def entrance(num):
    # Handle special cases
    if num <= 1:
        return False
    if num <= 3:
        return True

    # Check if number is divisible by any integer from 2 to the square root of the number
    i = 2
    while i * i <= num:
        if num % i == 0:
            return False
        i += 1

    return True