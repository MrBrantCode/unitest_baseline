"""
QUESTION:
Write a function named `search_keyword` that takes two arguments: `string` and `keyword`, and returns a list of indices where the keyword is found in the string. The search should be case insensitive, and the keyword should be surrounded by word boundaries (i.e., not part of a larger word).
"""

import re

def search_keyword(string, keyword):
    keyword = r"\b" + re.escape(keyword) + r"\b"
    matches = re.finditer(keyword, string, re.IGNORECASE)
    indices = [match.start() for match in matches]
    return indices