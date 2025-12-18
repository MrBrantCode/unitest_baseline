"""
QUESTION:
Implement a function named `is_anagram` that takes two strings as input, removes non-alphabetic characters, and returns True if the strings are anagrams of each other (i.e., contain the same characters, regardless of order), and False otherwise. The comparison should be case-insensitive.
"""

import re

def is_anagram(str1, str2):
    str1 = str1.lower()
    str2 = str2.lower()
    
    str1 = re.sub(r'[^a-z]', '', str1)
    str2 = re.sub(r'[^a-z]', '', str2)
    
    sorted_str1 = sorted(str1)
    sorted_str2 = sorted(str2)
    
    if len(sorted_str1) != len(sorted_str2):
        return False
    for i in range(len(sorted_str1)):
        if sorted_str1[i] != sorted_str2[i]:
            return False
    
    return True