"""
QUESTION:
Write a function `fibonacci(n)` to calculate the nth Fibonacci number, where n is a positive integer. The function should use a recursive approach and have a time complexity of O(n^2).
"""

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        a = 0
        b = 1
        for i in range(2, n + 1):
            c = a + b
            a = b
            b = c
        return b