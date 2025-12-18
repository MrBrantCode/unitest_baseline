"""
QUESTION:
Write a function `check_substring` that takes two strings `base_string` and `sub_string` as input and returns `True` if `sub_string` appears in `base_string` at least twice, and `False` otherwise. The function should be case-insensitive, handle special characters and whitespace, and return `False` if `sub_string` is empty.
"""

def check_substring(base_string, sub_string):
    # Handle case when sub-string is empty
    if not sub_string:
        return False

    # Convert both strings to lowercase for case-insensitive comparison
    base_string = base_string.lower()
    sub_string = sub_string.lower()

    # Check if sub-string appears in the base string
    if sub_string in base_string:
        # Check if sub-string appears at least twice
        count = base_string.count(sub_string)
        if count >= 2:
            return True

    return False