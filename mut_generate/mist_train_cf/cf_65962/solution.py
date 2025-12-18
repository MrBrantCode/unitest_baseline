"""
QUESTION:
Create a function `extract_text(html_string)` that takes a string containing HTML tags as input and returns the text within the tags, excluding the tags themselves. The function should use regular expressions to achieve this.
"""

import re

def extract_text(html_string):
    pattern = re.compile('<.*?>')
    text = re.sub(pattern, '', html_string)
    return text