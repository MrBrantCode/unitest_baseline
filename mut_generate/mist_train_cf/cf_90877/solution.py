"""
QUESTION:
Write a function `is_anagram(str1, str2)` to determine if two given strings are anagrams. The function should be case-sensitive and ignore any spaces or special characters.
"""

def entance(str1, str2):
    # Remove spaces and special characters from both strings
    str1 = ''.join(e for e in str1 if e.isalnum())
    str2 = ''.join(e for e in str2 if e.isalnum())

    # Check if the sorted strings are equal
    return sorted(str1) == sorted(str2)