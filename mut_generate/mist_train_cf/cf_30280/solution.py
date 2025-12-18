"""
QUESTION:
Write a function `extractH6Text` that takes a string of HTML content as input and returns the text content of the `<h6>` tag with the class attributes "m-0 font-weight-bold text-primary". If the tag is not found or the class attributes do not match, the function should return "Tag not found".
"""

import re

def extractH6Text(html_content):
    pattern = r'<h6 class="m-0 font-weight-bold text-primary">(.*?)</h6>'
    match = re.search(pattern, html_content)
    if match:
        return match.group(1)
    else:
        return "Tag not found"