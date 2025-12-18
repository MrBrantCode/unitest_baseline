"""
QUESTION:
Write a function named `calculate_modulus` that takes two positive integers `n1` and `n2` as input parameters and returns the result of `n1 % n2` without using the modulus operator. The function should handle cases where the result could be negative due to integer division.
"""

def calculate_modulus(n1, n2):
    quotient = n1 // n2
    remainder = n1 - (n2 * quotient)
    return remainder