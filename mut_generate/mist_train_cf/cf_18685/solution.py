"""
QUESTION:
Write a function named `compare_strings` that takes two strings `s1` and `s2` as input and returns `True` if they are the same after removing leading/trailing whitespaces, punctuation marks, and special characters, and converting to lowercase.
"""

import re

def entrance(s1, s2):
    # Remove leading and trailing white spaces
    s1 = s1.strip()
    s2 = s2.strip()
    
    # Remove punctuation marks and special characters
    s1 = re.sub('[^a-zA-Z]', '', s1)
    s2 = re.sub('[^a-zA-Z]', '', s2)
    
    # Convert both strings to lowercase
    s1 = s1.lower()
    s2 = s2.lower()
    
    # Compare the strings
    return s1 == s2