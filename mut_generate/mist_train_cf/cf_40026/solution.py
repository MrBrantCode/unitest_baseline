"""
QUESTION:
Write a function `extractInfo(html)` that takes a string `html` representing HTML code as input and returns the content within the first `<div>` element with the class "info". The function should return an empty string if no such element is found.
"""

import re

def extractInfo(html: str) -> str:
    match = re.search(r'<div class="info">(.*?)</div>', html)
    if match:
        return match.group(1)
    else:
        return ""