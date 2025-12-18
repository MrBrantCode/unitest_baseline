"""
QUESTION:
Create a function called `fibonacci` that calculates the nth Fibonacci number, where n can be any integer (positive, negative, or zero). The Fibonacci sequence for positive indices is defined as 0, 1, 1, 2, 3, 5, 8, ..., and for negative indices, the formula remains the same but introduces a negative sign on every other term (-1, 1, -2, 3, -5, 8, -13, ...). The function should be optimized for efficiency, with a time complexity better than the naive recursive approach.
"""

def fibonacci(n, memo={}):
    if n in memo:
        return memo[n]
    if n == 0:
        return 0
    if n == 1 or n == -1:
        return 1
    if n > 0:
        result = fibonacci(n-1, memo) + fibonacci(n-2, memo)
    else: # for negative n
        result = (-1) ** (n + 1) * fibonacci(-n, memo)
    memo[n] = result
    return result