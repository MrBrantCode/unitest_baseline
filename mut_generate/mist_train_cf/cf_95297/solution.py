"""
QUESTION:
Write a function `compare_strings(s1, s2)` that compares two given strings, ignoring leading/trailing white spaces, punctuation marks, special characters, and case differences. Return `True` if the strings are the same and `False` otherwise.
"""

import re

def entance(s1, s2):
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