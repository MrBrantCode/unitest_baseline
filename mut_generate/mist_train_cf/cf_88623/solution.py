"""
QUESTION:
Create a function `contains_consecutively` that takes two strings `first_str` and `second_str` as arguments. The function should return a tuple where the first element is a boolean indicating whether `second_str` appears consecutively in `first_str` (case insensitive and considering only alphanumeric characters) and the second element is the total count of such occurrences. The function should have a time complexity of O(n), where n is the length of `first_str`.
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