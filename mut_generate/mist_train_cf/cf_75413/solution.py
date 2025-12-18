"""
QUESTION:
Write a function `find_divisor` that takes two arguments, `dividend` and `quotient`, and returns the divisor that results in the equation `dividend` divided by the divisor equals `quotient`. The function should return a number that, when used as the divisor, makes the equation valid.
"""

def find_divisor(dividend, quotient):
    divisor = dividend / quotient
    return divisor