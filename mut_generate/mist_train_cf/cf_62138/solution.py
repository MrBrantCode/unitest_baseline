"""
QUESTION:
Given a sequence of n elements, write a function `is_sorted` that checks whether the given sequence is sorted in ascending or descending order. The function should return True if the sequence is sorted, and False otherwise.
"""

def is_sorted(seq):
    return all(seq[i] <= seq[i+1] for i in range(len(seq)-1)) or all(seq[i] >= seq[i+1] for i in range(len(seq)-1))