"""
QUESTION:
Implement a function called `fibonacci` that takes an integer `n` as input and returns a list of the Fibonacci sequence up to the nth iteration. The Fibonacci sequence is a series of numbers where a number is the sum of the two preceding ones, usually starting with 0 and 1. The function should initialize the sequence with the first two numbers [0, 1] and then compute the remaining numbers up to the given index.
"""

def fibonacci(n):
    # First two numbers in fibonacci sequence
    fib_sequence = [0, 1]

    # Compute the remaining numbers of the sequence
    for i in range(2, n+1):
        fib_sequence.append(fib_sequence[i-1] + fib_sequence[i-2])
    return fib_sequence[:n]