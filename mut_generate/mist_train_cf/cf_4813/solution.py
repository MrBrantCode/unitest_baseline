"""
QUESTION:
Create a function `count_string_occurrences` that takes two strings `string1` and `string2` as input. The function should return the number of times `string1` is found within `string2` in a case-insensitive manner, considering only matches surrounded by spaces or punctuation marks. If `string2` is empty, the function should return -1. The function should also handle cases where `string1` is empty or contains non-alphabetical characters.
"""

import re

def count_string_occurrences(string1, string2):
    if string2 == "":
        return -1
    
    string1 = re.sub(r'[^a-zA-Z\s]', '', string1)
    string1 = string1.lower()
    string2 = string2.lower()
    
    pattern = r'(?<!\S)' + re.escape(string1) + r'(?!\S)'
    matches = re.findall(pattern, string2)
    return len(matches)