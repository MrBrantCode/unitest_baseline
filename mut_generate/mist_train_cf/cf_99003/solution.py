"""
QUESTION:
Create a function `arithmetic_sequence` that takes a list of numbers as input and returns a string representing the formula for the arithmetic sequence. The sequence can be of any length, with any starting number and common difference. The function should first check if the sequence has at least two numbers, then calculate the common difference and verify that all subsequent differences are equal. If the sequence is arithmetic, the function should return the formula `a + dn`, where `a` is the starting number and `d` is the common difference.
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
    return f"{a} + {d}n"