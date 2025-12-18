"""
QUESTION:
Write a function named `divide` that takes two parameters: `dividend` and `divisor`. The function should return the quotient and remainder of the division operation. The function should use integer division and modulus operations.
"""

def divide(dividend, divisor):
    quotient = dividend // divisor
    remainder = dividend % divisor
    return quotient, remainder