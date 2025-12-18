"""
QUESTION:
Write a function called `validate_string` that takes a string `s` as input and returns `True` if the string is entirely in lowercase letters, contains at least one lowercase letter, and does not contain any special characters or digits. The function should return `False` otherwise. The function should have a time complexity of O(n), where n is the length of the string.
"""

def validate_string(s):
    lowercase = False
    for c in s:
        if not c.islower() and not c.isalpha():
            return False
        if c.islower():
            lowercase = True
    return lowercase