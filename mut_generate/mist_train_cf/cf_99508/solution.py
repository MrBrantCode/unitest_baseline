"""
QUESTION:
Create a function named `arithmetic_sequence` that takes a list of numbers as input and returns the formula for generating the arithmetic sequence if the input sequence is arithmetic. The function should handle sequences of any length, with any starting number and common difference.
"""

def arithmetic_sequence(sequence):
    n = len(sequence)
    if n < 2:
        return "Sequence must have at least two numbers."
    d = sequence[1] - sequence[0]
    for i in range(2, n):
        if sequence[i] - sequence[i-1] != d:
            return "Sequence is not arithmetic."
    a = sequence[0]
    return f"The formula for this arithmetic sequence is: {a} + {d}n"