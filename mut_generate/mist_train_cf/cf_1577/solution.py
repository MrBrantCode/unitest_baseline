"""
QUESTION:
Implement a function `are_anagrams` that checks if two input strings are anagrams of each other. The function should return `True` if the strings are anagrams and `False` otherwise. The comparison should be case-insensitive and ignore non-alphabetic characters. The function should have a time complexity of O(n log n) and constant space complexity, where n is the length of the longest string. The implementation should handle strings with Unicode characters and large input strings efficiently.
"""

import re

def are_anagrams(str1, str2):
    # Convert strings to lowercase
    str1 = str1.lower()
    str2 = str2.lower()
    
    # Remove non-alphabetic characters
    str1 = re.sub(r'[^a-z]', '', str1)
    str2 = re.sub(r'[^a-z]', '', str2)
    
    # Sort the characters of both strings
    sorted_str1 = sorted(str1)
    sorted_str2 = sorted(str2)
    
    # Compare the sorted strings character by character
    return sorted_str1 == sorted_str2