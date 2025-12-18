"""
QUESTION:
Implement a function named `fibonacci` that takes an integer `n` as input and returns the `n`th Fibonacci number using a recursive approach. The function should handle base cases for `n` equal to 0 and 1, and for larger `n`, it should recursively calculate the Fibonacci number.
"""

def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)