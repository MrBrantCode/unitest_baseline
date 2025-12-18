"""
QUESTION:
Write a function named `is_anagram` that takes two string variables as input and returns `True` if they are anagrams of each other, `False` otherwise. The function should be case-sensitive and ignore any spaces or special characters.
"""

def is_anagram(str1, str2):
    # Remove spaces and special characters from both strings
    str1 = ''.join(e for e in str1 if e.isalnum())
    str2 = ''.join(e for e in str2 if e.isalnum())

    # Check if the sorted strings are equal
    return sorted(str1) == sorted(str2)