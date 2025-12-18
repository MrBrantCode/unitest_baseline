"""
QUESTION:
Create a function called `fibonacci(n)` that uses a recursive approach to find the nth Fibonacci number. The function should handle the base cases where `n` is less than or equal to 0 (return 0) and `n` is 1 (return 1). For all other values of `n`, the function should return the sum of the `(n-1)`th and `(n-2)`th Fibonacci numbers. Implement this function without using an iterative or memoization approach.
"""

def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)