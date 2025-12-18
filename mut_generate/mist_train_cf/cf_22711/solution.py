"""
QUESTION:
Implement a function named `fibonacci(n)` that takes an integer `n` as input and returns the n-th Fibonacci number using a recursive approach without using memoization. The Fibonacci sequence is defined where each number is the sum of the two preceding ones, with base cases `fibonacci(0) = 0` and `fibonacci(1) = 1`. The function should only use recursive calls to compute the Fibonacci number and should not store or reuse previously computed values.
"""

def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)