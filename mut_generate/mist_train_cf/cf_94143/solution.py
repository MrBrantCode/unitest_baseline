"""
QUESTION:
Create a function named `is_anagram` that takes two strings `str1` and `str2` as input. The function should compare the two strings to determine if they are anagrams of each other, ignoring any whitespace characters, being case insensitive, and ignoring any punctuation marks. It should return `True` if the strings are anagrams and `False` otherwise.
"""

import string

def is_anagram(str1, str2):
    # Remove whitespace characters and convert to lowercase
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()
    
    # Remove punctuation marks
    translator = str.maketrans("", "", string.punctuation)
    str1 = str1.translate(translator)
    str2 = str2.translate(translator)
    
    # Compare the sorted strings
    return sorted(str1) == sorted(str2)