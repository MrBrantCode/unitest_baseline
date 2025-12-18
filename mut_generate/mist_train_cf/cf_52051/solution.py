"""
QUESTION:
Create a function `check_anagram(string1, string2)` that determines whether two strings are anagrams, considering special characters and numbers, and ignoring capitalization. The function should return a boolean value.
"""

from collections import Counter

def check_anagram(string1, string2):
    if len(string1) != len(string2):
        return False
    s1_count = Counter(string1.lower())
    s2_count = Counter(string2.lower())
    if s1_count == s2_count:
        return True
    else:
        return False