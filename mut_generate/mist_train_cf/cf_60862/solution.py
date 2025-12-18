"""
QUESTION:
Write a function named `fibonacci(n)` that generates a Fibonacci sequence of length `n`, where each number is the sum of the two preceding ones, starting from 0 and 1.
"""

def fibonacci(n):
    sequence = [0, 1]
    while len(sequence) < n:
        sequence.append(sequence[-1] + sequence[-2])
    return sequence