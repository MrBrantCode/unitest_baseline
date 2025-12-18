"""
QUESTION:
Design a function named `factorial` that calculates the factorial of a non-negative integer `n`. The function should also accept two optional parameters: `power` (default value 1) and `modulo` (default value None). If `power` is provided, the function should calculate the factorial of `n` raised to the power of `power`. If `modulo` is also provided, the result should be the factorial of `n` raised to the power of `power`, all modulo `modulo`.
"""

def factorial(n, power=1, modulo=None):
    fact = 1
    for i in range(1, n+1):
        fact = (fact * (i ** power)) % modulo if modulo else fact * (i ** power)
    return fact