"""
QUESTION:
Write a function named `check_substring` that takes two strings as input, `base_string` and `sub_string`, and returns `True` if `sub_string` appears in `base_string` and `False` otherwise. The function should be case-insensitive, ignoring letter case when comparing the strings.
"""

def check_substring(base_string, sub_string):
    base_string = base_string.lower()
    sub_string = sub_string.lower()
    
    if sub_string in base_string:
        return True
    else:
        return False