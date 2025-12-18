"""
QUESTION:
Write a function `extractHTMLContent` that takes a string `html` as input and returns the text content inside the `<span>` tag with the class "nav-link-text". If the tag is not found or the class is not present, return "Class not found".
"""

import re

def extractHTMLContent(html):
    match = re.search(r'<span class="nav-link-text">(.*?)</span>', html)
    if match:
        return match.group(1)
    else:
        return "Class not found"