"""
QUESTION:
Generate a function `fibonacci_sequence(n)` that creates a list of the first 'n' numbers in the Fibonacci sequence, where each number is the sum of the two preceding ones, starting with 0 and 1. The function should return this list.
"""

def fibonacci_sequence(n):
    fib_sequence = [0, 1]

    while len(fib_sequence) < n:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])

    return fib_sequence[:n]