"""
QUESTION:
Develop a function `factorial(n, power=1, modulo=None)` that calculates the factorial of a non-negative integer `n`. The function should elevate the factorial to the power of `power` if supplied. If `modulo` is also supplied, the result should be the factorial of `n` elevated to the power of `power`, all modulo `modulo`. If `modulo` is not supplied, the function should operate without it. The function should handle cases where `n` is 0, and it should avoid dealing with very large numbers to prevent memory problems.
"""

def entance(n, power=1, modulo=None):
    fact = 1
    for i in range(1, n+1):
        fact *= i
        if modulo:
            fact %= modulo
    fact = fact ** power
    if modulo:
        fact %= modulo
    return fact