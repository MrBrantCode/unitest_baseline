"""
QUESTION:
Implement a function named `multiply` that takes two integers `x` and `y` as input and returns their product. The function should be able to handle the multiplication of exceedingly large integers.
"""

from decimal import Decimal

def multiply(x, y):
    return Decimal(x) * Decimal(y)