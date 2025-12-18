"""
QUESTION:
Create a function `fibonacci_sequence(n)` that takes a positive integer `n` as input and returns a Fibonacci sequence up to `n` in the form of a list. The Fibonacci sequence should not include numbers greater than or equal to `n`. The sequence should start with 0 and 1, and each subsequent number should be the sum of the two preceding numbers.
"""

def fibonacci_sequence(n):
    sequence = [0, 1]
    while sequence[-1] < n:
        sequence.append(sequence[-1] + sequence[-2])
    return sequence[:-1]