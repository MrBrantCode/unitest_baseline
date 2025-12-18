"""
QUESTION:
Implement a function `extract_urls(html: str) -> List[str]` that takes an HTML snippet as input and returns a list of unique URLs found within the snippet. The function should match URLs that start with "http://" or "https://" and end with a non-whitespace character or a double quote (").
"""

from typing import List
import re

def extract_urls(html: str) -> List[str]:
    url_pattern = r'(https?://\S+?)[\s">]'
    urls = re.findall(url_pattern, html)
    return list(set(urls))