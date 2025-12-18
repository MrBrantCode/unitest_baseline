"""
QUESTION:
Create a function `are_anagrams` that takes two string parameters, `str1` and `str2`, and returns a boolean value indicating whether the two strings are anagrams of each other. The function should be case-sensitive and consider spaces, punctuation, and special characters as part of the string. The strings only contain alphabetical symbols.
"""

def are_anagrams(str1, str2):
    return sorted(str1) == sorted(str2)