"""
QUESTION:
Create a function `extract_link_text(html: str) -> List[str]` that takes a string `html` representing well-formed HTML content and returns a list of strings containing the text within the `<a>` tags, ignoring any leading or trailing whitespace.
"""

from typing import List
import re

def extract_link_text(html: str) -> List[str]:
    pattern = r'<a\s[^>]*>(.*?)</a>'
    matches = re.findall(pattern, html)
    return [match.strip() for match in matches]