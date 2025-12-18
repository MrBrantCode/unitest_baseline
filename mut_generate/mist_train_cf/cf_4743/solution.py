"""
QUESTION:
Create a function `contains_consecutively` that takes two strings, `first_str` and `second_str`, as arguments and returns a tuple containing a boolean and an integer. The function should check if `second_str` appears consecutively in `first_str` (case-insensitive and considering only alphanumeric characters), and return `True` along with the count of consecutive occurrences if found, or `False` with a count of 0 if not found. The function should have a time complexity of O(n), where n is the length of `first_str`.
"""

import re

def contains_consecutively(first_str, second_str):
    # Convert both strings to lowercase and remove non-alphanumeric characters
    first_str = re.sub(r'[^a-zA-Z0-9]', '', first_str.lower())
    second_str = re.sub(r'[^a-zA-Z0-9]', '', second_str.lower())

    count = 0
    i = 0
    while i < len(first_str):
        if first_str[i:i+len(second_str)] == second_str:
            count += 1
            i += len(second_str)
        else:
            i += 1
    
    return count > 0, count