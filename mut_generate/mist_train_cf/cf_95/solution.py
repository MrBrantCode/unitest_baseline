"""
QUESTION:
Create a function `extract_pattern` that takes two parameters: `text` (the input string) and `pattern` (the pattern to extract). If `pattern` is a single character, extract it from `text` only when it is surrounded by spaces or punctuation marks. If `pattern` is a substring, extract it from `text` only when it is surrounded by punctuation marks. The function should return the extracted pattern as a string, or an empty string if no match is found.
"""

import re

def extract_pattern(text, pattern):
    if len(pattern) == 1:
        pattern = re.escape(pattern)  # Escape special characters
        regex = r"(?<!\S)" + pattern + r"(?!\S)"
    else:
        pattern = re.escape(pattern)  # Escape special characters
        regex = r"(?<!\w)" + pattern + r"(?!\w)"
    
    match = re.search(regex, text)
    if match:
        return match.group()
    else:
        return ""