"""
QUESTION:
Write a function named `is_substring(s1, s2)` that takes two strings `s1` and `s2` and checks if `s2` is a substring of `s1` while being case-sensitive and ignoring leading and trailing whitespaces in both strings. The function should also handle empty strings and special characters. Return `True` if `s2` is a substring of `s1`, and `False` otherwise.
"""

def is_substring(s1, s2):
    s1 = s1.strip()
    s2 = s2.strip()
    
    if s1 == "" or s2 == "":
        return False
    
    s1 = ''.join(e for e in s1 if e.isalnum())
    s2 = ''.join(e for e in s2 if e.isalnum())
    
    return s2 in s1