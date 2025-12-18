"""
QUESTION:
Write a function named `check_substring` that takes two strings as input, `base_string` and `sub_string`. The function should return `True` if `sub_string` appears in `base_string` at least twice, regardless of case, special characters, or whitespace. The function should also return `False` if `sub_string` is empty, appears only once, or does not appear in `base_string`.
"""

def check_substring(base_string, sub_string):
    if not sub_string:
        return False

    base_string = base_string.lower()
    sub_string = sub_string.lower()

    if sub_string in base_string:
        count = base_string.count(sub_string)
        if count >= 2:
            return True

    return False