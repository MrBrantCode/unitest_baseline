"""
QUESTION:
Create a function named `count_occurrences` that takes two strings as input: `string1` and `string2`. The function should return the number of times `string1` is found within `string2`, with the following conditions: 
- The search should be case-insensitive.
- If `string2` is empty, return -1.
- If `string1` is empty, return 0.
- `string1` may contain non-alphabetical characters or special characters, which should be treated as literal characters.
- A match is only counted if it is surrounded by spaces or punctuation marks.
"""

import re

def count_occurrences(string1, string2):
    if string2 == "":
        return -1

    if string1 == "":
        return 0

    pattern = r"(?<![^\W_])" + re.escape(string1) + r"(?![^\W_])"
    matches = re.findall(pattern, string2, re.IGNORECASE)
    return len(matches)