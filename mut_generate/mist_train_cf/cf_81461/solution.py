"""
QUESTION:
Write a function `fibonacci(n, memo={})` that calculates the nth number in the Fibonacci sequence using recursion and memoization. The function should return the nth Fibonacci number. The Fibonacci sequence is defined such that each number is the sum of the two preceding ones, starting from 0 and 1. The function should use memoization to store already calculated values and avoid redundant calculations.
"""

def fibonacci(n, memo={}):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    elif n not in memo:
        memo[n] = fibonacci(n-1, memo) + fibonacci(n-2, memo)
    return memo[n]