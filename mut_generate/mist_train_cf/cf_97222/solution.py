"""
QUESTION:
Implement a function named `fibonacci(n)` that calculates the n-th Fibonacci number using a recursive approach without using memoization. The function should take an integer `n` as input and return the corresponding Fibonacci number. The function should be based on the definition of the Fibonacci sequence where each number is the sum of the two preceding ones.
"""

def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)