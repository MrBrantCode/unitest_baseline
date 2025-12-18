"""
QUESTION:
Create a function called `fibonacci` that generates the Fibonacci sequence. The Fibonacci sequence is a numerical series where each digit is the sum of the preceding two. The function should take an integer `n` as input and return the first `n` numbers in the sequence.
"""

def fibonacci(n):
    sequence = [0, 1]
    while len(sequence) < n:
        sequence.append(sequence[-1] + sequence[-2])
    return sequence