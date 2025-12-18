"""
QUESTION:
Write a function `extractClassValue` that takes a string representing an HTML tag as input and returns the value of the class attribute. The HTML tag is in the format `<tagname class="class-value">`, where the class attribute value does not contain any quotes and may contain multiple classes separated by spaces. If the class attribute is not present, the function should return `None`.
"""

import re

def extractClassValue(html_tag):
    match = re.search(r'class="([^"]+)"', html_tag)
    if match:
        return match.group(1)
    else:
        return None