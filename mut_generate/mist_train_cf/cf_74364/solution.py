"""
QUESTION:
Write a function `invert_sequence(seq)` that takes a list of integers `seq` as input and returns the inverted sequence. The function should optimize for both speed and space complexity. The input sequence is guaranteed to contain at least 1000 integers.
"""

def invert_sequence(seq):
    """
    Returns the inverted sequence of the given list of integers.

    Args:
    seq (list): A list of integers.

    Returns:
    list: The inverted sequence of the input list.
    """
    return seq[::-1]