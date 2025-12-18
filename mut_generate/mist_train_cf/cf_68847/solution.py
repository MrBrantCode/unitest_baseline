"""
QUESTION:
Create a Python function named `factorial(n, power=1, modulo=None)` that calculates the factorial of a non-negative integer `n`. The function should have two optional parameters: `power` to elevate the factorial to a certain power, and `modulo` to calculate the result modulo a certain number. If `power` is not provided, it defaults to 1. If `modulo` is not provided, the function should not perform the modulo operation. The function should correctly handle all possible combinations of the three parameters.
"""

def entance(n, power=1, modulo=None):
    fact = 1
    for i in range(1, n+1):
        fact *= i
    fact = fact ** power
    if modulo:
        return fact % modulo
    return fact