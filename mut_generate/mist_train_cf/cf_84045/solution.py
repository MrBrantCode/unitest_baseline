"""
QUESTION:
Write a function `sum_of_digits(n, power=1, modulo=None)` that takes a non-negative integer `n` and two optional arguments, `power` and `modulo`. The function should return the sum of the digits of `n` raised to the power of `power` and, if `modulo` is provided, the result modulo `modulo`. If `power` or `modulo` is not provided, it should default to 1 and None respectively. The function should handle all possible combinations of the three arguments.
"""

def sum_of_digits(n, power=1, modulo=None):
    result = 0
    for digit in str(n):
        result += int(digit) ** power
    if modulo:
        return result % modulo
    else:
        return result