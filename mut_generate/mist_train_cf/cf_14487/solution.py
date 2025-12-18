"""
QUESTION:
Write a function `check_strings(str1, str2)` that takes two strings as input and returns `True` if the length of `str1` is equal to the length of `str2` and both strings contain only lowercase alphabetic characters, and `False` otherwise. Assume the input strings are not `None`.
"""

def check_strings(str1, str2):
    # Check if both strings contain only lowercase alphabetic characters
    if not str1.isalpha() or not str2.isalpha() or not str1.islower() or not str2.islower():
        return False
    
    # Check if the length of the first string is equal to the length of the second string
    if len(str1) != len(str2):
        return False
    
    return True