"""
QUESTION:
Write a function `reverse_seq` that takes a list of integers as input and returns the reversed list without using the built-in `reverse()` function. The function should be able to handle lists with up to 10^6 elements and complete execution in under 2 seconds.
"""

def reverse_seq(seq):
    """
    Reverses a given list of integers.
    
    Args:
    seq (list): A list of integers to be reversed.
    
    Returns:
    list: The reversed list of integers.
    """
    return [seq[i] for i in range(len(seq)-1, -1, -1)]