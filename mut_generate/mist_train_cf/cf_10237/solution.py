"""
QUESTION:
Write a function `fibonacci_sequence(n)` that generates the Fibonacci sequence of length `n`, where `n` is a prime number between 10 and 100, and the sequence starts with the initial two numbers, 0 and 1. The function should return the Fibonacci sequence as a list of integers.
"""

def fibonacci_sequence(n):
    sequence = [0, 1]  # Initialize the Fibonacci sequence with the first two numbers

    while len(sequence) < n:
        next_num = sequence[-1] + sequence[-2]  # Calculate the next number in the sequence
        sequence.append(next_num)  # Add the next number to the sequence

    return sequence