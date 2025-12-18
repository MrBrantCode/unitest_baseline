"""
QUESTION:
Create a function named `divide` that takes two parameters: `dividend` and `divisor`. The function should return the quotient and remainder of the division operation. The function must use integer division (quotient in which the digits after the decimal point are not taken into account) and the modulus operator (remainder of the division).
"""

def divide(dividend, divisor):
    """Return the quotient and remainder of the division operation."""
    quotient = dividend // divisor
    remainder = dividend % divisor
    return quotient, remainder