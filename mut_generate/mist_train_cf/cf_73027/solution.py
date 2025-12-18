"""
QUESTION:
Write a function `are_lexical_anagrams(seq1, seq2)` that checks if two given alpha-numeric sequences are lexical anagrams, disregarding spaces and punctuation. The function should be case sensitive and handle sequences of different lengths efficiently. It should return `True` if the sequences are anagrams and `False` otherwise. The input sequences may contain uppercase and lowercase letters, numbers, and special characters.
"""

from collections import Counter
import re

def are_lexical_anagrams(seq1, seq2):
    """
    Checks if two given alpha-numeric sequences are lexical anagrams, 
    disregarding spaces and punctuation. The function is case sensitive 
    and handles sequences of different lengths efficiently.

    Args:
        seq1 (str): The first alpha-numeric sequence.
        seq2 (str): The second alpha-numeric sequence.

    Returns:
        bool: True if the sequences are anagrams, False otherwise.
    """

    seq1 = re.sub('[^A-Za-z0-9]+', '', seq1)
    seq2 = re.sub('[^A-Za-z0-9]+', '', seq2)

    return Counter(seq1) == Counter(seq2)