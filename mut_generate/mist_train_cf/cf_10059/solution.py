"""
QUESTION:
Write a function `fibonacci(n)` that uses recursion to calculate the nth number in the Fibonacci sequence. The Fibonacci sequence is defined such that each number is the sum of the two preceding ones, starting from 0 and 1. The function should return the nth Fibonacci number. Note that the input `n` will be a non-negative integer.
"""

def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)