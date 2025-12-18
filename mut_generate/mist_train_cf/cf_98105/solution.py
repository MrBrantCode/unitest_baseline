"""
QUESTION:
Write an iterative function `fibonacci_iterative` that calculates the nth Fibonacci number. The function should have a time complexity of O(n) and use constant memory space.
"""

def fibonacci_iterative(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        a, b = 0, 1
        for _ in range(2, n+1):
            c = a + b
            a = b
            b = c
        return b