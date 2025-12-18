"""
QUESTION:
Implement a memoized recursive function named `fibonacci` that calculates the nth number in the Fibonacci sequence, where the function takes an integer `n` and an optional dictionary `memo` as arguments. The function should return the calculated Fibonacci number. The function must use memoization to store the results of previous calculations to avoid redundant computations.
"""

def fibonacci(n, memo={}):
    if n in memo:
        return memo[n]
    if n == 0 or n == 1:
        result = n
    else:
        result = fibonacci(n-1, memo) + fibonacci(n-2, memo)
    memo[n] = result
    return result