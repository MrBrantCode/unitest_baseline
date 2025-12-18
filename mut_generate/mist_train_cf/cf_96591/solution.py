"""
QUESTION:
Write a function named `reverse_string` that takes a string as input, removes any non-alphanumeric characters, and returns the reversed string. The function should use slicing to reverse the string.
"""

import re

def reverse_string(s):
    # Remove special characters
    s = re.sub('[^A-Za-z0-9]+', '', s)
    
    # Reverse the string
    return s[::-1]