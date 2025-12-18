"""
QUESTION:
Write a function `factorial(n, memo = {})` that calculates the factorial of a non-negative integer `n` using memoization to store intermediate results and avoid repetitive calculations.
"""

def factorial(n, memo = {}):
    if n < 2: 
        return 1
    if not n in memo: 
        memo[n] = n * factorial(n-1, memo)
    else: 
        print(f"Using memoized value for factorial of {n}")
    return memo[n]