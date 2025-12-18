"""
QUESTION:
Create a function called `factorial(n)` that calculates the factorial of a given integer `n`. The function should return the factorial of `n` if `n` is a non-negative integer, and a message indicating that the factorial is not defined if `n` is negative. The function should not use recursion to calculate the factorial.
"""

def entance(n):
    if n == 0:
        return 1
    elif n < 0:
        return "Factorial is not defined for negative numbers"
    else:
        result = 1
        for i in range(1, n+1):
            result *= i
        return result