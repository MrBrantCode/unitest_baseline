"""
QUESTION:
Write a function `exponential_notation` that takes a number as input and returns its equivalent exponential notation if it exists. The function should find a base number that can be multiplied by itself a certain number of times to get the input number.
"""

import math

def exponential_notation(n):
    for base in range(2, int(math.sqrt(n)) + 1):
        exp = 2
        while base ** exp <= n:
            if base ** exp == n:
                return f"{base}^{exp}"
            exp += 1
    return None