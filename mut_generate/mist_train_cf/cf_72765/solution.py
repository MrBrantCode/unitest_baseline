"""
QUESTION:
Write a function `compute_fibonacci_series(n)` that generates a Fibonacci series with a specified limit of 'n' elements, where each element is the sum of the two preceding ones. The series should start with 0 and 1.
"""

def compute_fibonacci_series(n):
    fib_series = []
    a, b = 0, 1
    while len(fib_series) < n:
        fib_series.append(a)
        a, b = b, a + b
    return fib_series