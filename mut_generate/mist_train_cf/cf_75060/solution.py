"""
QUESTION:
Write a function `merge_sequences(seq1, seq2)` that merges two numerical sequences and removes duplicates while preserving the original order. The function should take two sequences as input and return a single sequence containing all elements from both sequences without any duplicates.
"""

def merge_sequences(seq1, seq2):
    seen = set()
    result = [x for x in seq1+seq2 if not (x in seen or seen.add(x))]
    return result