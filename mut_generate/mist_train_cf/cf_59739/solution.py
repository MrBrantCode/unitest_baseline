"""
QUESTION:
Write a function `factorial(n, power=1, modulo=None)` that calculates the factorial of a non-negative integer `n`. The function should handle two optional parameters: `power` and `modulo`. If `power` is provided, the function should compute the factorial of `n` raised to the power of `power`. If `modulo` is also provided, the function should compute the result modulo `modulo`. If either `power` or `modulo` is not provided, the function should perform accordingly. Ensure the function handles potential overflow issues when computing large powers.
"""

def entance(n, power=1, modulo=None):
    fact = 1
    for i in range(1, n+1):
        fact *= pow(i, power, modulo) if modulo else i ** power
    return fact if not modulo else fact % modulo