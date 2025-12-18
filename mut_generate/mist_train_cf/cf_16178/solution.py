"""
QUESTION:
Create a recursive function `fibonacci(n)` that takes a positive integer `n` as input and returns the `n`th number in the Fibonacci sequence without using loops, memoization techniques, or built-in functions such as `range()`. The function should handle the base cases where `n` is 0 or 1 and return `n` itself. For other values of `n`, the function should recursively call itself to compute the `n`th Fibonacci number.
"""

def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)