"""
QUESTION:
Calculate the cumulative total of the digital sums of the first one hundred decimal digits for all non-integer square roots of the initial one hundred positive integers.

The function `digital_sum` should take an integer as input and return the sum of the first one hundred decimal digits of its square root. If the square root is a whole number, it should be excluded from the calculation. The result should be calculated with high precision to account for rounding errors.
"""

from decimal import getcontext, Decimal

getcontext().prec = 102

def digital_sum(n):
    s = str(Decimal(n).sqrt()).replace('.', '')[:100]
    return sum(int(d) for d in s)