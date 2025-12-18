"""
QUESTION:
Construct a function named `sum_of_digits` that takes a non-negative integer `n` and two optional parameters: `power` (default is 1) and `modulo` (default is None). The function should return the sum of the digits of `n` if only `n` is provided. If `power` is provided, the function should return the sum of the digits of `n` raised to the power of `power`. If `power` and `modulo` are provided, the function should return the sum of the digits of `n` raised to the power of `power`, with each term taken modulo `modulo` before being added to the sum.
"""

def sum_of_digits(n, power=1, modulo=None):
    sum = 0
    for digit in str(n):
        if modulo:
            sum += (int(digit) ** power) % modulo
        else:
            sum += int(digit) ** power
    return sum