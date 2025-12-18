"""
QUESTION:
Generate a function `fibonacci(n)` that returns the first `n` numbers in the Fibonacci sequence, where each number is the sum of the two preceding ones, starting with the first two numbers as 1 and 1. The function should be able to handle a large input value of `n`, such as 1,000,000.
"""

def fibonacci(n):
    fib_sequence = [1, 1]  # Initialize with the first two numbers
    for i in range(2, n):
        fib_sequence.append(fib_sequence[i-1] + fib_sequence[i-2])
    return fib_sequence