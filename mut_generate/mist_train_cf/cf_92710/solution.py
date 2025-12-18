"""
QUESTION:
Write a function named `is_anagram(s1, s2)` that takes two strings `s1` and `s2` as input and returns a boolean value indicating whether the two strings are anagrams of each other. Consider all characters in the strings, including spaces and punctuation marks, and take their case into account. The function should return True if the strings are anagrams, otherwise return False.
"""

def is_anagram(s1, s2):
    # Check if the sorted strings are equal
    return sorted(s1) == sorted(s2)