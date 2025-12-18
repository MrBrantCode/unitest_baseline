"""
QUESTION:
Create a function `extract_pattern` that takes two parameters: `text` (the input string) and `pattern` (the pattern to extract). The function should return the extracted pattern from the text if it matches the specified rules. The pattern should only match when it is surrounded by spaces or punctuation marks if it's a single character, or when it's surrounded by punctuation marks if it's a substring.
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