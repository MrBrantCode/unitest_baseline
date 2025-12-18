"""
QUESTION:
Write a function `remove_html_tags(html: str) -> str` that takes a string `html` of length between 1 and 10^5 containing HTML tags, and returns a string with all HTML tags removed.
"""

import re

def remove_html_tags(html: str) -> str:
    clean_text = re.sub(r'<[^>]*>', '', html)  # Use regular expression to remove all HTML tags
    return clean_text