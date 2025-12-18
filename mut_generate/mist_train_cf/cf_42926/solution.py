"""
QUESTION:
Implement a function `extract_html_tags(html_snippet: str) -> List[str]` that takes a well-formed HTML snippet as input and returns a list of unique HTML tag names present in the snippet. The function should extract tag names, which are defined as the strings that appear between the angle brackets '<' and '>', and return them as a list of strings. The list should not contain duplicate tag names.
"""

from typing import List
import re

def extract_html_tags(html_snippet: str) -> List[str]:
    tag_names = re.findall(r'<([^\s>/]+)', html_snippet)
    return list(set(tag_names))