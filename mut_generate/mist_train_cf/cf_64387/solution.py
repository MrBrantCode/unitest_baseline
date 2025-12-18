"""
QUESTION:
Write a recursive function `fibonacci(n)` that generates the `n`th Fibonacci number. The function should take a positive integer `n` as input, with the following base cases: `fibonacci(1)` returns 0 and `fibonacci(2)` returns 1. For `n` greater than 2, the function should return the sum of `fibonacci(n-1)` and `fibonacci(n-2)`.
"""

def entance(n):
    if n <= 0:
        return "Input should be a positive integer."
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return entance(n-1) + entance(n-2)