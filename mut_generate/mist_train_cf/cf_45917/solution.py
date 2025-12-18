"""
QUESTION:
Write a function `is_anagram(str1, str2)` that determines if two input strings are anagrams of each other. The function should ignore case, spaces, and punctuation, and consider only alphanumeric characters. It should return `True` if the strings are anagrams and `False` otherwise.
"""

def is_anagram(str1, str2):
    # Remove all non-alphanumeric characters and convert to lower case
    str1 = ''.join(e for e in str1 if e.isalnum()).lower()
    str2 = ''.join(e for e in str2 if e.isalnum()).lower()
    
    # Return comparison of sorted strings
    return sorted(str1) == sorted(str2)