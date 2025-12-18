"""
QUESTION:
Write a recursive function `factorial(n)` that calculates the factorial of a given number `n` using memoization to store previously computed results, with the restriction that the function calls itself to compute the factorial. The function should return the factorial of the input number `n`.
"""

def factorial(n, memo = {}):
    if n not in memo:
        if n == 0:
            memo[n] = 1
        else:
            memo[n] = n * factorial(n-1, memo)
    return memo[n]