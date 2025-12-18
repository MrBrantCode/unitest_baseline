"""
QUESTION:
Write a function `compress_string(s)` that takes a string `s` as input, removes special characters (keeping only letters, digits, and spaces), and compresses the string by removing repeated characters while preserving the original case. The function should not treat 'A' and 'a' as the same character.
"""

import re

def compress_string(s):
    # Remove special characters
    s = re.sub('[^A-Za-z0-9 ]+', '', s)
    
    # Remove repeated characters
    s = ''.join([s[i] for i in range(len(s)) if i == 0 or s[i] != s[i-1]])
    
    return s