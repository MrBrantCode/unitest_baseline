"""
QUESTION:
Write a function `check_anagram(str1, str2)` that checks if `str2` is an anagram of `str1`, considering case sensitivity and special characters, and including spaces and punctuation as relevant characters.
"""

def check_anagram(str1, str2):
    # Sorting both the strings and then comparing
    return sorted(str1) == sorted(str2)