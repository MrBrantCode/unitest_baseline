"""
QUESTION:
Create a function `greatest_common_divisor(a, b)` that takes two integers as arguments and returns their greatest common divisor using the Euclidean algorithm.
"""

def greatest_common_divisor(a, b):
    while b != 0:
        a, b = b, a % b
    return a