"""
QUESTION:
Create a function named `evaluate_string` that takes a string as input. The function should return True if the string contains at least 3 consecutive uppercase letters, and False otherwise. The function should also return False if the string contains any special characters or if there are no consecutive uppercase letters. The function is case-sensitive, meaning that lowercase letters are not considered as consecutive uppercase letters.
"""

import re

def evaluate_string(string):
    # Check if string contains special characters
    if not re.match(r'^[a-zA-Z0-9_]*$', string):
        return False
    
    # Check if string contains at least 3 consecutive uppercase letters
    for i in range(len(string) - 2):
        if string[i].isupper() and string[i+1].isupper() and string[i+2].isupper():
            return True
    
    return False