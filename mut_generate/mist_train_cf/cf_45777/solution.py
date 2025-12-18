"""
QUESTION:
Design a function `factorial(n, power=1, modulo=None)` that calculates the factorial of a non-negative integer `n`. 

If `power` is provided, the function should return the factorial of `n` raised to the power of `power`. If `modulo` is also provided, the function should return the result modulo `modulo`. 

The function should handle large inputs efficiently, negative powers, and negative modulo values, and should be optimized for time complexity.
"""

def entance(n, power=1, modulo=None):
    fact = 1
    for i in range(1, n+1):
        fact *= i
        if modulo:
            fact %= abs(modulo)
    if power < 0:
        fact = 1 / (fact ** abs(power))
    else:
        fact = fact ** power 
    if modulo:
        fact %= abs(modulo)
    return fact