"""
QUESTION:
Write a function named `is_anagram` that takes two input strings `str1` and `str2` and checks if `str2` is an anagram of `str1`. The function should remove all spaces and special characters from the input strings before checking for anagrams, and it should handle strings that are case-sensitive. The function should return `True` if `str2` is an anagram of `str1` and `False` otherwise. The function should be efficient and able to handle large input strings without causing memory or performance issues.
"""

import string

def is_anagram(str1, str2):
    # Remove spaces and special characters
    str1 = ''.join(char for char in str1 if char.isalnum())
    str2 = ''.join(char for char in str2 if char.isalnum())

    # Check if lengths are different
    if len(str1) != len(str2):
        return False

    # Create frequency dictionaries
    freq1 = {}
    freq2 = {}

    # Count character frequencies in str1
    for char in str1:
        freq1[char.lower()] = freq1.get(char.lower(), 0) + 1

    # Count character frequencies in str2
    for char in str2:
        freq2[char.lower()] = freq2.get(char.lower(), 0) + 1

    # Compare character frequencies
    return freq1 == freq2