"""
QUESTION:
Write a function `extract_html_tags(html_code: str) -> List[str]` that takes a string of well-formed HTML code with balanced tags and returns a list of unique HTML tag names present in the code snippet.
"""

from typing import List
import re

def extract_html_tags(html_code: str) -> List[str]:
    tag_pattern = re.compile(r'<\s*([a-zA-Z0-9]+)[^>]*>')
    tags = tag_pattern.findall(html_code)
    unique_tags = list(set(tags))
    return unique_tags