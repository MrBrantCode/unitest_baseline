"""
QUESTION:
Implement a function `fibonacci(n)` that calculates the nth number in the Fibonacci sequence using memoization, with a time complexity better than O(2^n) and returns the calculated value. The Fibonacci sequence is a series of numbers in which each number is the sum of the two preceding numbers, starting from 0 and 1.
"""

memo = {0: 0, 1: 1}

def fibonacci(n):
    if n not in memo:
        memo[n] = fibonacci(n-1) + fibonacci(n-2)
    return memo[n]