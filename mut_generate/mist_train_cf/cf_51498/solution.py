"""
QUESTION:
Write a function named `backward_sequence_union` that takes two sequences of integers as input and returns their backward sequence union. The function should combine the two sequences, remove duplicates while maintaining the original order, and reverse the sequence. The function should work for integer type data and should be implemented in Python 3.7 or later.
"""

def backward_sequence_union(seq1, seq2):
    seq1 += seq2
    seq1.reverse()
    return list(dict.fromkeys(seq1))