"""
QUESTION:
Write a function `is_subsequence(s1, s2)` that takes two string sequences as input and returns `True` if `s1` is a subsequence of `s2`, meaning all characters in `s1` appear in `s2` in the same order, and `False` otherwise.
"""

def is_subsequence(s1, s2):
    """
    Checks if s1 is a subsequence of s2.
    
    Args:
        s1 (str): The potential subsequence.
        s2 (str): The original sequence.
    
    Returns:
        bool: True if s1 is a subsequence of s2, False otherwise.
    """
    # Initialize counters
    i = j = 0
    
    # Iterate through the strings
    while i < len(s1) and j < len(s2):
        if s1[i] == s2[j]:
            i += 1
        j += 1
    
    # If all characters of s1 were found in s2 in original order,
    # then s1 is subsequence of s2
    return i == len(s1)