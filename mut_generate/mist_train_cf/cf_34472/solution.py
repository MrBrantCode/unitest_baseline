"""
QUESTION:
Write a function named `extract_urls` that takes a string of HTML as input and returns a list of URLs found in anchor tags. The input string will be between 1 and 100,000 characters in length, and URLs will be enclosed in double quotes after the `href` attribute in anchor tags.
"""

from typing import List
import re

def extract_urls(html: str) -> List[str]:
    pattern = r'href="([^"]*)"'
    urls = re.findall(pattern, html)
    return urls