"""
QUESTION:
Write a function `fibonacci(n)` that calculates the nth Fibonacci number using recursion, where `n` is a positive integer representing the position in the Fibonacci sequence. The function should return the nth Fibonacci number if `n` is 1 or greater, and it should handle cases where `n` is less than or equal to 0.
"""

def fibonacci(n):
    if n <= 0:
        return "Incorrect input"
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)