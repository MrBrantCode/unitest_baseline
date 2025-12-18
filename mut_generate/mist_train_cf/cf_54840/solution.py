"""
QUESTION:
Design a function called `sort_and_count` that takes a string `s` as input and returns a new string. The function should sort the alphabets in the string in alphabetical order (case-insensitive), count the frequency of each alphabet, and output these frequencies. Non-alphabet characters in the string should be placed at the end of the new string in the order they originally appeared.
"""

from collections import Counter

def sort_and_count(s):
    # Split characters into alphabets and non-alphabets
    alphabets = [c for c in s if c.isalpha()]
    non_alphabets = [c for c in s if not c.isalpha()]

    # Sort and count alphabets
    alphabets = sorted(alphabets, key=str.lower)
    count = Counter(alphabets)

    # Combine and return new string
    new_s = ''.join(alphabets + non_alphabets)
    return new_s