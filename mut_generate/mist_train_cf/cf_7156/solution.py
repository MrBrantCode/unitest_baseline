"""
QUESTION:
Implement a function called `fibonacci` that takes an integer `n` as input and returns the nth number in the Fibonacci sequence. The Fibonacci sequence is a series of numbers in which each number is the sum of the two preceding ones. The function should use memoization to store the results of expensive function calls and reuse them when the same inputs occur again, thus avoiding redundant calculations.
"""

def fibonacci(n, cache={}):
    if n <= 1:
        return n
    elif n not in cache:
        cache[n] = fibonacci(n-1, cache) + fibonacci(n-2, cache)
    return cache[n]