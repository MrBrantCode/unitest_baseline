"""
QUESTION:
Create a function `fibonacci(n)` that calculates the nth number in the Fibonacci sequence. The function should be recursive, have a time complexity of O(2^n), and not use any loops, memoization techniques, built-in functions, additional data structures, or global variables. If `n` is negative, return `None`.
"""

def fibonacci(n):
    if n < 0:
        return None
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)