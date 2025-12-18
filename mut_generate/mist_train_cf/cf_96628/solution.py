"""
QUESTION:
Write a function named `fibonacci` that returns the sum of the first n Fibonacci numbers. The Fibonacci sequence is a series of numbers where a number is the sum of the two preceding ones, usually starting with 0 and 1. The function should take an integer `n` as input and return the sum of the first `n` numbers in the Fibonacci sequence.
"""

def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

def fibonacci_sum(n):
    return sum(fibonacci(i) for i in range(n + 1))