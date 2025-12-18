"""
QUESTION:
Create a function `are_anagrams(str1, str2)` that determines if two input strings are anagrams of each other. The function should return `True` if the strings are anagrams and `False` otherwise. The comparison should be case-sensitive unless otherwise specified.
"""

def are_anagrams(str1, str2):
    return sorted(str1) == sorted(str2)