"""
QUESTION:
Create a function `is_anagram(str1, str2)` that checks if two strings are anagrams of each other. The function should ignore spaces, punctuation marks, and case differences, and it should efficiently handle large input strings with lengths up to 10^6 characters. The function should return True if the strings are anagrams and False otherwise.
"""

import string
from collections import Counter

def is_anagram(str1, str2):
    # Remove spaces and punctuation marks, and convert to lowercase
    str1 = str1.translate(str.maketrans('', '', string.punctuation)).replace(" ", "").lower()
    str2 = str2.translate(str.maketrans('', '', string.punctuation)).replace(" ", "").lower()
    
    # Check if the length of both strings are equal
    if len(str1) != len(str2):
        return False
    
    # Check if the frequency of each character is the same in both strings
    return Counter(str1) == Counter(str2)