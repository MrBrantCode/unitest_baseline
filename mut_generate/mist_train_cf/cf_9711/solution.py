"""
QUESTION:
Create a function `fibonacci(n)` to find the nth number in the Fibonacci sequence. The function should be recursive, not use any loops, and not use memoization techniques. The function should return the nth number if n is greater than 0, and None otherwise.
"""

def fibonacci(n):
    if n <= 0:
        return None
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)