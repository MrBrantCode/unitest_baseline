"""
QUESTION:
Write a function `is_anagram` that takes two strings as input and returns `True` if they are anagrams of each other, and `False` otherwise. The function should be case-insensitive, ignore non-alphanumeric characters, and support strings written in different languages and scripts.
"""

import unicodedata

def is_anagram(string1, string2):
    # Remove non-alphanumeric characters and convert to lowercase
    processed_string1 = ''.join(c for c in unicodedata.normalize('NFKD', string1) if unicodedata.category(c).startswith('L') or c.isdigit()).lower()
    processed_string2 = ''.join(c for c in unicodedata.normalize('NFKD', string2) if unicodedata.category(c).startswith('L') or c.isdigit()).lower()
    
    # Sort the processed strings
    sorted_string1 = sorted(processed_string1)
    sorted_string2 = sorted(processed_string2)
    
    # Compare the sorted strings
    return sorted_string1 == sorted_string2