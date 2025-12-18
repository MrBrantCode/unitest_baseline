"""
QUESTION:
Write a function called `factorial` that calculates the factorial of a given number `n` using a recursive algorithm without any loops or iterative constructs, and returns the result modulo 10^9+7.
"""

def factorial(n):
    if n == 0:
        return 1
    else:
        return (n * factorial(n-1)) % (10**9 + 7)