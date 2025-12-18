"""
QUESTION:
Write a function `factorial_memoization(n, memo = {})` that calculates the factorial of a given non-negative integer `n` using memoization, ensuring each calculation is performed only once to enhance efficiency. The function should store previously computed factorials in the `memo` dictionary and return the factorial of `n`.
"""

def factorial_memoization(n, memo={}):
    if n == 0: 
        return 1 
    if n in memo: 
        return memo[n] 
    else:
        result = n * factorial_memoization(n - 1, memo)
        memo[n] = result 
        return result