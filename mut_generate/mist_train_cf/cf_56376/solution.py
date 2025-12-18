"""
QUESTION:
Create a recursive function called `factorial` that calculates the factorial of a given integer `n` using memoization to store previously computed factorial values. The function should have a default argument `memo` that is an empty dictionary.
"""

def factorial(n, memo={}):
    if n < 2:
        return 1
    if n not in memo:
        memo[n] = n * factorial(n-1, memo)
    return memo[n]