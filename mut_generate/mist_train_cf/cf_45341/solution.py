"""
QUESTION:
Write a function `sum_of_digits(n, power=1, modulo=None, multiplier=1)` that calculates the sum of the digits of a non-negative integer `n`. The function should raise the sum of the digits to the power of `power` if provided. If `modulo` is provided, the result should be taken modulo `modulo`. If `multiplier` is provided, the result should be multiplied by `multiplier`. The function should handle all combinations of these optional arguments correctly.
"""

def sum_of_digits(n, power=1, modulo=None, multiplier=1):
    sum_digs = 0
    for digit in str(n):
        sum_digs += int(digit) ** power
    sum_digs *= multiplier
    if modulo:
        sum_digs %= modulo
    return sum_digs