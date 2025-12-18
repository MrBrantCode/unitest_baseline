"""
QUESTION:
Write a function `fibonacci(n)` that calculates the nth Fibonacci number. The function should not use any built-in mathematical functions or libraries and should have a time complexity of O(n) due to the inherent nature of the Fibonacci sequence.
"""

def fibonacci(n):
    memo = {0: 0, 1: 1}
    for i in range(2, n + 1):
        memo[i] = memo[i - 1] + memo[i - 2]
    return memo[n]