"""
QUESTION:
Write a function named `check_substring` that takes two strings as input, `base_string` and `sub_string`, and returns `True` if `sub_string` appears in `base_string` and `False` otherwise. The function should be case-insensitive, ignoring the letter case when comparing the sub-string with the base string.
"""

def check_substring(base_string, sub_string):
    # Convert both strings to lowercase for case-insensitive comparison
    base_string = base_string.lower()
    sub_string = sub_string.lower()
    
    # Check if the sub-string appears in the base string
    return sub_string in base_string