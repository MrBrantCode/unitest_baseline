"""
QUESTION:
Write a function called `fibonacci(n)` that takes a single positive integer `n` as input and returns the `n`-th Fibonacci number. The function should handle the cases where `n` is 1 or 2, and return the sum of the `(n-1)`-th and `(n-2)`-th Fibonacci numbers for `n` greater than 2.
"""

def fibonacci(n):
    if n <= 0:
        print("Input should be a positive integer")
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)