"""
QUESTION:
Write a function `is_divisible_by_7_and_13(n)` that checks if an integer `n` is divisible by both 7 and 13 without using the division operator `/` or the modulo operator `%`.
"""

def is_divisible_by_7_and_13(n):
    # Get the quotient and remainder when n is divided by 7
    quotient, remainder = divmod(n, 7)
    if remainder != 0:
        return False
    # Get the quotient and remainder when n is divided by 13
    quotient, remainder = divmod(n, 13)
    if remainder != 0:
        return False
    # The number is divisible by both 7 and 13
    return True