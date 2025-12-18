"""
QUESTION:
Write a function `fibonacci(n)` that generates and returns the Fibonacci series of length `n`. The Fibonacci series is a series of numbers where each number after the first two is the sum of the two preceding ones.
"""

def fibonacci(n):
    fib_series = [0, 1]    # Starting elements
    while len(fib_series) < n:
        fib_series.append(fib_series[-1] + fib_series[-2])
    return fib_series