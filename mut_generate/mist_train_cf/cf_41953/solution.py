"""
QUESTION:
Write a function `extract_urls_from_html(html)` that takes a string `html` representing well-formed HTML code as input, where the `href` attribute in anchor tags is always enclosed in double quotes, and returns a list of URLs extracted from the anchor tags. Assume that the anchor tags may contain other nested HTML elements, but the `href` attribute will always be directly within the `<a>` tag.
"""

import re

def extract_urls_from_html(html):
    pattern = r'<a\s+href="([^"]+)"'
    urls = re.findall(pattern, html)
    return urls