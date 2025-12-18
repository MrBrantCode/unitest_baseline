"""
QUESTION:
Write a function `is_anagram(s1, s2)` that checks whether string `s1` is an anagram of string `s2`, considering letter case. The function should return `True` if `s1` is an anagram of `s2`, and `False` otherwise.
"""

def is_anagram(s1, s2):
    # Convert both strings to lowercase
    s1 = s1.lower()
    s2 = s2.lower()

    # Sort the characters in both strings
    s1 = sorted(s1)
    s2 = sorted(s2)

    # Check if the sorted strings are equal
    return s1 == s2