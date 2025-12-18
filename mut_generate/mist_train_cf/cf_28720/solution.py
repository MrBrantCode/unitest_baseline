"""
QUESTION:
Create a function `extract_hyperlinks(markdown_text: str) -> List[Tuple[str, str]]` that takes a Markdown text as input and returns a list of tuples, where each tuple contains the URL and its anchor text. The function should handle cases where there are multiple hyperlinks in the Markdown text and correctly extract both the URL and the anchor text for each hyperlink.
"""

from typing import List, Tuple
import re

def extract_hyperlinks(markdown_text: str) -> List[Tuple[str, str]]:
    pattern = r'\[([^\]]+)\]\(([^)]+)\)'
    matches = re.findall(pattern, markdown_text)
    return matches