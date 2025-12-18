"""
QUESTION:
Implement a function called `is_prime` that determines whether a given number is a prime number. The function should not use the modulo operator (%) and should be able to handle any integer as input.
"""

import math

def entrance(number):
    if number <= 1:
        return False

    for i in range(2, int(math.sqrt(number)) + 1):
        if number / i == int(number / i):
            return False

    return True