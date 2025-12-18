"""
QUESTION:
Write a function called `generate_fibonacci(n)` that generates and returns the Fibonacci sequence of a given length `n`. The Fibonacci sequence is a series of numbers where a number is the addition of the last two numbers, starting with 0 and 1. The function should return a list containing the first `n` numbers of the Fibonacci sequence.
"""

def generate_fibonacci(n):
    fibonacci_sequence = [0, 1]

    while len(fibonacci_sequence) < n:
        fibonacci_sequence.append(fibonacci_sequence[-1] + fibonacci_sequence[-2])

    return fibonacci_sequence[:n]