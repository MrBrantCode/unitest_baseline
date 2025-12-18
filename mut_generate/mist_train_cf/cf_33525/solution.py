"""
QUESTION:
Create a function `count_html_tags(html_snippet: str, tags: List[str]) -> Dict[str, int]` that takes in a string representing an HTML snippet and a list of HTML tags as input. The function should return a dictionary where the keys are the HTML tags provided in the input list (case-insensitive) and the values are the counts of occurrences of each tag within the HTML snippet. The function should assume that the input HTML snippet is well-formed and does not contain nested tags of the same type.
"""

from typing import List, Dict
import re

def count_html_tags(html_snippet: str, tags: List[str]) -> Dict[str, int]:
    tag_counts = {}
    for tag in tags:
        pattern = rf'<{tag}.*?>'
        count = len(re.findall(pattern, html_snippet, re.IGNORECASE))
        tag_counts[tag.lower()] = count
    return tag_counts