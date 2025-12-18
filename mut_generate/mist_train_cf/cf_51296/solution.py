"""
QUESTION:
Create a function `isAnagram(s1, s2)` that takes two strings `s1` and `s2` as input, including alphanumeric and non-alphanumeric characters, and returns `True` if `s1` is an anagram of `s2` (regardless of case, order, and special characters), and `False` otherwise.
"""

from collections import Counter

def isAnagram(s1, s2):
    return Counter(s1.lower().replace(" ", "").replace(",", "").replace(".", "")) == Counter(s2.lower().replace(" ", "").replace(",", "").replace(".", ""))