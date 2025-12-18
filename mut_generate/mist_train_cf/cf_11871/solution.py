"""
QUESTION:
Write a function called `fibonacci` that takes an integer `n` as input and returns the Fibonacci sequence for the first `n` numbers using recursion in a functional programming style.
"""

def fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        sequence = fibonacci(n - 1)
        return sequence + [sequence[-1] + sequence[-2]]