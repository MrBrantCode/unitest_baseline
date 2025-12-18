"""
QUESTION:
Implement a function `fibo(n)` that calculates the nth Fibonacci number, where the Fibonacci sequence is a series of numbers in which each number is the sum of the two preceding ones, starting with 0 and 1. The function should take an integer `n` as input and return the corresponding Fibonacci number. The input `n` must be a positive integer.
"""

def fibo(n):
    if n <= 0:
        return "Invalid input"
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        a, b = 0, 1
        for _ in range(2, n):
            a, b = b, a + b
        return b