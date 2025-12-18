"""
QUESTION:
Create a function named `sort_descending` that takes a sequence of floating-point numbers as input, sorts the sequence in descending order, and returns the sorted list.
"""

def sort_descending(seq):
    seq.sort(reverse=True)
    return seq