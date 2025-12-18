"""
QUESTION:
Implement a function `is_happy(s)` that takes a string `s` as input and returns `True` if it represents happiness and `False` otherwise. A string is classified as happy if it has a minimum length of 3, every group of three successive characters are distinct, each discrete character appears at least twice, with no single character manifesting three consecutive times, and the string contains only alphanumeric characters. If the string contains non-alphanumeric characters, return an error message.
"""

import re

def is_happy(s):
    """ This function takes a string s as input and returns True if it represents happiness and False otherwise."""
    
    # Check if the string contains only alphanumeric characters
    if not s.isalnum():
        return "Invalid input string! Only alphanumeric characters are allowed."
    
    n = len(s)
    
    # The string must have at least a length of 3 for it to be happy
    if n < 3: return False
    
    # Check that every group of three successive characters are distinct
    for i in range(n-2):
        if len(set(s[i:i+3])) != 3:
            return False
    
    # Check that each discrete character appears not less than twice
    char_count = {}
    for char in s:
        char_count[char] = char_count.get(char, 0) + 1
    if min(char_count.values()) < 2:
        return False
     
    # Check that no character appears three times consecutively
    if re.search(r'(.)\1\1', s):
        return False
    
    return True