"""
QUESTION:
Construct the `fibonacci` function that generates the nth Fibonacci number using a recursive method and memoization. The function should take an integer `n` as input and return the corresponding Fibonacci number. Implement memoization to optimize the solution for larger inputs.
"""

def fibonacci(n, memo={}):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n not in memo:
        memo[n] = fibonacci(n-1, memo) + fibonacci(n-2, memo)
    return memo[n]