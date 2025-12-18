"""
QUESTION:
Develop a function `is_fibonacci(n)` that takes an integer `n` as input and returns `True` if `n` is a Fibonacci number and `False` otherwise. Use this function to filter a given list of numbers and return a new list containing only the Fibonacci numbers from the original list.
"""

def is_fibonacci(n):
    x = 0
    y = 1
    while y < n:
        z = x + y
        x = y
        y = z
    return y == n or n == 0