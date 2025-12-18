"""
QUESTION:
Write a function `are_anagrams(s1, s2)` that checks if two given alpha-numeric sequences are lexical anagrams, ignoring case, punctuation, and whitespace. The function should return `True` if the sequences are anagrams, and `False` otherwise.
"""

from collections import Counter

def are_anagrams(s1, s2):
    # Make inputs case-insensitive
    s1 = s1.lower()
    s2 = s2.lower()
    
    # Remove punctuation and whitespace
    s1 = ''.join(e for e in s1 if e.isalnum())
    s2 = ''.join(e for e in s2 if e.isalnum())

    # Count character frequencies and compare
    return Counter(s1) == Counter(s2)