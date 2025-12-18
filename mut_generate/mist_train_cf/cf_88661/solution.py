"""
QUESTION:
Write a function `count_string_occurrences` that takes two strings, `string1` and `string2`, as input and returns the number of times `string1` is found within `string2`. The function should perform a case-insensitive search, handle empty strings properly, and count only matches of `string1` that are surrounded by spaces or punctuation marks. If `string2` is empty, the function should return -1.
"""

import re

def count_string_occurrences(string1, string2):
    if string2 == "":
        return -1
    
    string1 = re.sub(r'[^a-zA-Z\s]', '', string1)
    string1 = string1.lower()
    string2 = string2.lower()
    
    count = 0
    pattern = r'(?<!\S)' + string1 + r'(?!\S)'
    matches = re.findall(pattern, string2)
    count = len(matches)
    
    return count