"""
QUESTION:
Create a function `sum_of_digits(n, power=1, modulo=None)` that calculates the sum of the digits of a non-negative whole number `n`. The function should have two optional parameters: `power` and `modulo`. If `power` is provided, each digit should be raised to that power before being added to the sum. If `modulo` is provided, the final sum should be taken modulo that value. If either `power` or `modulo` is not provided, the function should still operate correctly.
"""

def sum_of_digits(n, power=1, modulo=None):
    sum = 0
    for digit in str(n):
        temp = int(digit) ** power
        if modulo:
            temp %= modulo
        sum += temp
        if modulo:
            sum %= modulo
    return sum