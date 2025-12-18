"""
QUESTION:
Write a function `iterative_fibonacci(n)` that calculates the nth Fibonacci number using an iterative approach. The function should take an integer `n` as input and return the corresponding Fibonacci number. The function should not use recursion.
"""

def iterative_fibonacci(n):
    a = 0
    b = 1
    for i in range(n):
        a, b = b, a + b
    return a