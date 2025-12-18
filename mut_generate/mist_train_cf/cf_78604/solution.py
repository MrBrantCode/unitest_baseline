"""
QUESTION:
Write a function `count_subsequence(seq, sub)` that takes a sequence of characters `seq` and a specific subsequence `sub` as input, and returns the number of non-overlapping occurrences of `sub` within `seq`. The function is case-sensitive.
"""

def count_subsequence(seq, sub):
    """
    This function counts the number of non-overlapping occurrences of a subsequence within a sequence.
    
    Parameters:
    seq (str): The full sequence of characters.
    sub (str): The specific subsequence to count.
    
    Returns:
    int: The number of non-overlapping occurrences of the subsequence.
    """
    count = seq.count(sub)
    return count