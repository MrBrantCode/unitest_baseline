"""
QUESTION:
Write a function called `fibonacci(n)` that calculates the Fibonacci sequence up to `n` numbers, where `n` is a positive integer, and returns the sequence as a list. The Fibonacci sequence starts with 0 and 1, and each subsequent number is the sum of the previous two.
"""

def fibonacci(n):
    sequence = [0, 1]
    while len(sequence) < n:
        sequence.append(sequence[-1] + sequence[-2])
    return sequence[:n]