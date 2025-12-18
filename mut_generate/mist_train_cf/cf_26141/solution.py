"""
QUESTION:
Extract text inside HTML div tags using a regular expression. Write a function `extract_div_text` that captures any characters (including none) between the opening and closing div tags in a non-greedy manner. The input string will contain HTML tags, and the function should return the text inside the div tags.
"""

import re

def extract_div_text(html_string):
    pattern = r"<div>(.*?)</div>"
    match = re.search(pattern, html_string, re.DOTALL)
    if match:
        return match.group(1)
    else:
        return None