"""
QUESTION:
Create a function named `Fibonacci` and `Lucas` that generates and displays the initial `n` constituents of the Fibonacci series and Lucas numbers, respectively. The Fibonacci series is a sequence where each number is the sum of the two preceding ones, starting with 0 and 1. The Lucas numbers follow a similar rule but start with 2 and 1. The input `n` should be a user-defined value ranging from 1 to 10000. The function must handle inputs up to 10000 without exceeding Python's maximum recursion depth, suggesting an iterative approach is required.
"""

def Fibonacci(n):
    """Generate the initial n constituents of the Fibonacci series."""
    fibonacci_series = [0, 1]
    while len(fibonacci_series) < n:
        fibonacci_series.append(fibonacci_series[-1] + fibonacci_series[-2])
    return fibonacci_series[:n]

def Lucas(n):
    """Generate the initial n constituents of the Lucas numbers."""
    lucas_series = [2, 1]
    while len(lucas_series) < n:
        lucas_series.append(lucas_series[-1] + lucas_series[-2])
    return lucas_series[:n]