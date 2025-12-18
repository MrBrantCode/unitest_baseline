"""
QUESTION:
Create a function `extract_html_content(html: str) -> List[str]` that takes an HTML snippet as input and returns a list of all the text content within the HTML tags. The input `html` is a string (1 <= len(html) <= 1000) consisting of one or more HTML tags with text content. The output should be a list of strings, where each string represents the text content within an HTML tag.
"""

from typing import List
import re

def extract_html_content(html: str) -> List[str]:
    pattern = r'>([^<]+)<'
    matches = re.findall(pattern, html)
    return matches