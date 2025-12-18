"""
QUESTION:
Create a function named 'is_anagram' that takes two strings 'str1' and 'str2' as input. The function should return True if 'str1' and 'str2' are anagrams of each other, False otherwise. The function should be case-sensitive, handle whitespace characters, special characters, strings of different lengths, and non-alphanumeric characters. It should have a time complexity of O(n), where n is the length of the longer string. If either of the input strings is empty, the function should return False. If either of the input strings is None, the function should return False.
"""

import re

def is_anagram(str1, str2):
    if str1 is None or str2 is None:
        return False
    if len(str1) == 0 or len(str2) == 0:
        return False
    
    str1 = str1.replace(" ", "")
    str2 = str2.replace(" ", "")
    str1 = re.sub(r'\W+', '', str1)
    str2 = re.sub(r'\W+', '', str2)
    
    if len(str1) != len(str2):
        return False
    
    sorted_str1 = sorted(str1)
    sorted_str2 = sorted(str2)
    
    return sorted_str1 == sorted_str2