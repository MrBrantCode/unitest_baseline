"""
QUESTION:
Implement a function called `fibonacci` that takes an integer `n` as input and returns the nth Fibonacci number. The Fibonacci sequence is defined as the first two numbers being 0 and 1, and each subsequent number is the sum of the previous two numbers. Use recursion and memoization to improve efficiency, without using any loops or iteration.
"""

def fibonacci(n, memo={}):
    if n in memo:
        return memo[n]
    if n == 0:
        return 0
    if n == 1:
        return 1
    memo[n] = fibonacci(n-1, memo) + fibonacci(n-2, memo)
    return memo[n]