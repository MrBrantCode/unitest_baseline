"""
QUESTION:
Create a function called `geometric_sequence` that generates a unique geometric sequence of numbers given the first term (`start`), the common ratio (`ratio`), and the length of the sequence (`length`). The function should return a list of numbers where each term after the first is found by multiplying the previous term by the `ratio`. The `start`, `ratio`, and `length` parameters must be unique for each sequence generation.
"""

def geometric_sequence(start, ratio, length):
    seq = [start]
    while len(seq) < length:
        seq.append(seq[-1] * ratio)
    return seq