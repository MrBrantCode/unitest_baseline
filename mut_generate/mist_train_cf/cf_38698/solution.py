"""
QUESTION:
Create a function `extract_urls(html)` that takes a string `html` representing HTML code as input and returns a list of URLs extracted from the "href" attribute within each anchor tag. The function should be able to handle multiple anchor tags and assumes that the anchor tags are well-formed and have the "href" attribute for the URLs.
"""

import re

def extract_urls(html):
    pattern = r'<a\s+[^>]*href=["\']([^"\']*)["\'][^>]*>'
    urls = re.findall(pattern, html)
    return urls