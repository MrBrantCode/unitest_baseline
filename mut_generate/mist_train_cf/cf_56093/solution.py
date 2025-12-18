"""
QUESTION:
Write a function named `rearrange_sequence` that takes a sequence of integers as input and returns a new sequence where the integers are arranged in descending order. The function should not modify the original sequence.
"""

def rearrange_sequence(seq):
    return sorted(seq, reverse=True)