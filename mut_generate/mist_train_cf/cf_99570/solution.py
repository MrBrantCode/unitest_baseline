"""
QUESTION:
Write a Python function named `divide` that takes two parameters: `dividend` and `divisor`. The function should return the quotient and remainder of the division operation. The function should use integer division to calculate the quotient and the modulus operator to calculate the remainder.
"""

def divide(dividend, divisor):
    quotient = dividend // divisor
    remainder = dividend % divisor
    return quotient, remainder