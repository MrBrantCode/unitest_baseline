"""
QUESTION:
Create a function named `is_anagram` that takes two phrases as input and returns `True` if they are anagrams of each other, considering phrases with different letter cases, lengths, and punctuation marks as anagrams. The function should be case-insensitive and ignore punctuation marks.
"""

import re
from collections import Counter

def is_anagram(phrase1, phrase2):
    """
    Returns True if two phrases are anagrams of each other, 
    considering phrases with different letter cases, lengths, and punctuation marks as anagrams.

    Args:
    phrase1 (str): The first phrase.
    phrase2 (str): The second phrase.

    Returns:
    bool: True if the phrases are anagrams, False otherwise.
    """
    
    # Remove punctuation marks and convert to lowercase
    phrase1 = re.sub(r'[^\w\s]', '', phrase1).lower()
    phrase2 = re.sub(r'[^\w\s]', '', phrase2).lower()

    # Count the frequency of each letter in both phrases
    freq1 = Counter(phrase1)
    freq2 = Counter(phrase2)

    # Check if the frequencies of all letters are the same
    return freq1 == freq2