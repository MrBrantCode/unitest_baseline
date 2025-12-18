"""
QUESTION:
Create a function named `fibonacci` that takes an integer `n` as input and returns the nth Fibonacci number. The function should have a time complexity of O(n) and a space complexity of O(1), allowing it to efficiently handle large values of `n`.
"""

def fibonacci(n):
    a, b, c = 0, 1, 0
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        for _ in range(2, n+1):
            c = a + b
            a = b
            b = c
        return c