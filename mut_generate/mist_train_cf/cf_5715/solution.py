"""
QUESTION:
Write a function called `fibonacci` that calculates the nth Fibonacci number using a recursive approach. The Fibonacci sequence is a series of numbers where each number is the sum of the two preceding ones, starting with 0 and 1. The function should take one integer argument `n` and return the corresponding Fibonacci number. The function must not use memoization. The input `n` will be in the range 0 <= n <= 1000.
"""

def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)