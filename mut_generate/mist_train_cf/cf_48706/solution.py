"""
QUESTION:
Write a function called `sum_of_digits` that calculates the sum of the digits of a non-negative integer. The function should take two arguments: a non-negative integer `n` and an optional integer `power`. If `power` is not provided, return the sum of the digits. If `power` is provided, return the sum of the digits raised to the power of `power`.
"""

def sum_of_digits(n, power=None):
    digits = [int(d) for d in str(n)]
    if power is None:
        return sum(digits)
    else:
        return sum([d**power for d in digits])