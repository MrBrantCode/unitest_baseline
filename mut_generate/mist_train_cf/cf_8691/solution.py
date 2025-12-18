"""
QUESTION:
Create a function named `evaluate_string` that takes a string as input and returns a boolean value. The function should return `True` if the string contains at least 3 consecutive uppercase letters, and `False` otherwise. The function should be case-sensitive and should also return `False` if the string contains any special characters other than letters, numbers, and underscores.
"""

import re

def evaluate_string(s):
    if not re.match(r'^[a-zA-Z0-9_]*$', s):
        return False
    
    for i in range(len(s) - 2):
        if s[i].isupper() and s[i+1].isupper() and s[i+2].isupper():
            return True
    
    return False