"""
QUESTION:
Write a function named `fibonacci` that calculates numbers in the Fibonacci sequence. The function should take an integer `n` as input and return the nth number in the sequence, where `fibonacci(0) = 0` and `fibonacci(1) = 1`. The Fibonacci sequence is defined such that each number is the sum of the two preceding ones.
"""

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)