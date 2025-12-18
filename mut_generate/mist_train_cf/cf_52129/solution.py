"""
QUESTION:
Write a function named `fibonacci(n)` that generates and returns a list of the first `n` numbers in the Fibonacci sequence, given a positive integer `n`. The function should be able to handle any positive integer input.
"""

def fibonacci(n):
    fib_sequence = [0, 1]
    while len(fib_sequence) < n:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence[:n]