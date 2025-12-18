"""
QUESTION:
Write a function `test_anagram(s1, s2)` that takes two strings as input and returns a boolean indicating whether the two input strings are anagrams of each other. The function should consider only the characters in the strings, ignoring any order. Assume both input strings only contain lowercase letters.
"""

def test_anagram(s1, s2):
    return sorted(s1) == sorted(s2)