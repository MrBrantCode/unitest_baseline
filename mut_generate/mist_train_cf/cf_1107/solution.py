"""
QUESTION:
Create a function named `is_anagram` that takes two strings `str1` and `str2` as input. The function should return `True` if the two strings are anagrams and `False` otherwise. The function should be case-sensitive, handle whitespace and special characters, and have a time complexity of O(n), where n is the length of the longer string. The function should also handle strings of different lengths, Unicode characters, and multi-byte characters. If either of the input strings is empty or `None`, the function should return `False`.
"""

import re

def is_anagram(str1, str2):
    if str1 is None or str2 is None:
        return False
    if len(str1) == 0 or len(str2) == 0:
        return False
    
    str1 = re.sub(r'\W+', '', str1)
    str2 = re.sub(r'\W+', '', str2)
    
    return sorted(str1) == sorted(str2)