"""
QUESTION:
Write a function `count_html_tags(html_snippet: str) -> dict` that takes an HTML snippet as a string and returns a dictionary mapping each unique HTML tag to its occurrence count in the snippet. Assume the input HTML snippet is well-formed, valid, and tags are not nested within each other.
"""

import re

def count_html_tags(html_snippet: str) -> dict:
    tag_counts = {}
    tags = re.findall(r'<(\w+)', html_snippet)  
    for tag in tags:
        tag = tag.lower()  
        tag_counts[tag] = tag_counts.get(tag, 0) + 1  
    return tag_counts