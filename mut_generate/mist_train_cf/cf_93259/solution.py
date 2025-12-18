"""
QUESTION:
Construct a function named `check_strings` that takes two strings `str1` and `str2` as input. The function should return `True` if both strings have the same length and only contain lowercase alphabetic characters, and `False` otherwise. The function should assume that the input strings are not `None`.
"""

def check_strings(str1, str2):
    # Check if both strings contain only lowercase alphabetic characters
    if not str1.islower() or not str2.islower():
        return False
    
    # Check if the length of the first string is equal to the length of the second string
    if len(str1) != len(str2):
        return False
    
    return True