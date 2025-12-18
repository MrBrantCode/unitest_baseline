"""
QUESTION:
Write a function named `factorial` that calculates the factorial of a given number `n` using recursion and memoization. The function should store previously computed factorial values in a dictionary called `memo` to avoid redundant calculations. The base case for the recursion is when `n` equals 0, in which case the function should return 1.
"""

def factorial(n, memo={}):
    if n == 0:
        return 1
    elif n in memo:
        return memo[n]
    else:
        memo[n] = n * factorial(n-1)
        return memo[n]