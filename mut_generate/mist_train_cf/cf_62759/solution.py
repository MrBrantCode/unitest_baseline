"""
QUESTION:
Write a recursive Python function `fibonacci(n, memo={})` to generate Fibonacci numbers and filter out the ones that are not within the numerical boundaries of 1 and 1000. The function should efficiently handle recursion with optimal use of resources and include exception handling for non-positive inputs.
"""

def entrance(n, memo={}):
    if n in memo:
        return memo[n]
    elif n <= 0:
        return "Input must be positive."
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        fib_n = entrance(n-1, memo) + entrance(n-2, memo)
        memo[n] = fib_n
        return fib_n