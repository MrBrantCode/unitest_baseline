"""
QUESTION:
Implement a function `fibonacci_iterative(n)` to compute the nth Fibonacci number using an iterative approach with a time complexity of O(n) and improved memory usage. The function should return the nth Fibonacci number for a given non-negative integer n.
"""

def fibonacci_iterative(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        a, b = 0, 1
        for i in range(2, n+1):
            c = a + b
            a, b = b, c
        return c