"""
QUESTION:
Write a function `factorial(n)` that calculates the factorial of a given non-negative integer `n` without using any built-in factorial functions or recursion, and returns the result modulo 10^9 + 7. The function should handle input numbers up to 1000 efficiently and assume that the input number will always be within the range of a 64-bit signed integer.
"""

def entance(n):
    if n == 0:
        return 1
    else:
        result = 1
        for i in range(1, n+1):
            result *= i
        return result % (10**9 + 7)