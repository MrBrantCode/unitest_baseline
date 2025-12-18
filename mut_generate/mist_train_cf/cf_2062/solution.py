"""
QUESTION:
Create a function `fibonacci(n)` that calculates the nth Fibonacci number modulo 10^9 + 7 using a non-recursive approach, where n is a positive integer up to 10^12.
"""

def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, (a + b) % (10**9 + 7)
        return b