"""
QUESTION:
Write a function named `fibonacci` that takes an integer `n` as input and returns the n-th Fibonacci number using a recursive approach without using memoization. The Fibonacci sequence is defined such that each number is the sum of the two preceding ones, starting from 0 and 1.
"""

def fibonacci(n):
    # Base case for n = 0 or 1
    if n <= 1:
        return n

    # Recursive case
    return fibonacci(n-1) + fibonacci(n-2)