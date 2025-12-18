"""
QUESTION:
Write a function `fibonacci_iterative(n)` that calculates the nth Fibonacci number using an iterative approach with a time complexity of O(n) and constant memory space. The function should return the nth Fibonacci number.
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