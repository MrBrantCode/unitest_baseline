"""
QUESTION:
Create a function `extract_pattern(text, pattern)` that takes two parameters: `text` and `pattern`. The function should return the `pattern` if it exists in the `text` and is surrounded by spaces or punctuation marks, or is not part of a larger word. If the `pattern` is a single character, it should only match when it is surrounded by spaces or punctuation marks.
"""

import re

def extract_pattern(text, pattern):
    # Escape special characters in the pattern
    pattern = re.escape(pattern)
    
    # Create the regex pattern
    regex_pattern = r"(?<![a-zA-Z0-9_])" + pattern + r"(?![a-zA-Z0-9_])"
    
    # Find all matches in the text
    matches = re.findall(regex_pattern, text)
    
    # Return the matches as a string
    return "".join(matches)