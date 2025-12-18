"""
QUESTION:
Write a function named `validate_string` that takes a string `s` as input. The function should return `True` if the string contains only lowercase letters and at least one lowercase letter, and `False` otherwise. The function should have a time complexity of O(n), where n is the length of the string.
"""

def validate_string(s):
    lowercase = False
    for c in s:
        if not c.islower() and not c.isalpha():
            return False
        if c.islower():
            lowercase = True
    return lowercase