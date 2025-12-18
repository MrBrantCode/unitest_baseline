"""
QUESTION:
Define a function `string_sequence(n)` that takes an integer `n` as input and returns a string of numbers from 0 to `n` (inclusive) separated by spaces.
"""

def string_sequence(n):
    sequence = []
    for i in range(n + 1):
        sequence.append(str(i))
    return ' '.join(sequence)