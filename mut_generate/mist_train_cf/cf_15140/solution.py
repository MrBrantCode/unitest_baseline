"""
QUESTION:
Write a function called `fibonacciRecursive` that takes an integer `n` as input and returns the nth Fibonacci number using a recursive approach with a time complexity of O(2^n).
"""

def fibonacciRecursive(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacciRecursive(n - 1) + fibonacciRecursive(n - 2)