"""
QUESTION:
Write a function `extract_urls(html_code: str) -> List[str]` that takes a string `html_code` representing an HTML snippet as input and returns a list of all the URLs extracted from the `href` attributes of the anchor tags. The HTML code will always contain well-formed anchor tags with `href` attributes, and the URLs are enclosed within double curly braces (`{{ }}`).
"""

from typing import List
import re

def extract_urls(html_code: str) -> List[str]:
    pattern = r'href="{{\s*([^{}]+)\s*}}"'
    matches = re.findall(pattern, html_code)
    return matches