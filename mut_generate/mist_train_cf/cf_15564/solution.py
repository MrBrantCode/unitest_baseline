"""
QUESTION:
Write a function `factorial(n)` to calculate the factorial of a given non-negative integer `n` and return the result modulo 10^9 + 7 without using any built-in factorial functions or recursion. The function should handle input numbers up to 1000 efficiently and assume the input is within the range of a 64-bit signed integer.
"""

def factorial(n):
    if n == 0:
        return 1
    else:
        result = 1
        for i in range(1, n+1):
            result = (result * i) % (10**9 + 7)
        return result