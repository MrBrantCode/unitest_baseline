"""
QUESTION:
Create a function called `divide` that takes two parameters, `dividend` and `divisor`, and returns the quotient and remainder of the division operation. The function should use integer division for the quotient and the modulus operator for the remainder.
"""

def divide(dividend, divisor):
    quotient = dividend // divisor
    remainder = dividend % divisor
    return quotient, remainder