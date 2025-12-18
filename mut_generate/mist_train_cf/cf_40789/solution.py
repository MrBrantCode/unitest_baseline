"""
QUESTION:
Write a function `extract_links(html_code: str) -> List[str]` that takes a string `html_code` representing an HTML code snippet as input and returns a list of URLs extracted from the anchor tags present in the HTML code. The input HTML code is guaranteed to be well-formed with anchor tags in the format `<a href="URL">Link Text</a>`, and the URLs in the `href` attribute may contain variables or placeholders enclosed in curly braces.
"""

from typing import List
import re

def extract_links(html_code: str) -> List[str]:
    href_pattern = r'href="([^"]+)"'
    href_matches = re.findall(href_pattern, html_code)
    return href_matches