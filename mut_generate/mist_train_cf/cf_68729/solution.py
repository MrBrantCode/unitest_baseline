"""
QUESTION:
Write a function `isAnagram(str1, str2)` that determines if two input strings are anagrams of each other. The function should consider both case sensitivity and special characters.
"""

from collections import Counter

def isAnagram(str1, str2):
    # Counter() function would produce a dictionary with characters as key and their counts as value.
    # If the dictionaries of both strings are equal, they are anagrams.
    return Counter(str1) == Counter(str2)