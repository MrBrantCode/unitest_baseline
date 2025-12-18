"""
QUESTION:
Create a function named `is_palindrome` that takes a string `s` as input and returns `True` if the string is a palindrome and `False` otherwise. The function should ignore spaces, punctuation, and capitalization.
"""

import re

def is_palindrome(s):
    # Remove spaces and punctuation
    s = re.sub(r'[^a-zA-Z0-9]', '', s)
    
    # Convert to lowercase
    s = s.lower()
    
    # Compare characters
    for i in range(len(s)//2):
        if s[i] != s[-i-1]:
            return False
    
    return True