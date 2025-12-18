"""
QUESTION:
Create a function called `has_consecutive_uppercase` that takes a string as input and returns `True` if the string contains at least 3 consecutive uppercase letters, and `False` otherwise.
"""

def has_consecutive_uppercase(s):
    for i in range(len(s)-2):
        if s[i:i+3].isupper():
            return True
    return False