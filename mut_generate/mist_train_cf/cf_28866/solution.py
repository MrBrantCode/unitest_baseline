"""
QUESTION:
Write a function `validateHTMLTag(tag)` that takes a string `tag` as input. The input string must adhere to the following rules: it starts with `<`, followed by a valid tag name consisting of letters (a-z, A-Z), digits (0-9), hyphens (-), underscores (_), or periods (.), optionally contains attribute-value pairs where each attribute is a valid tag name followed by `=` and a value enclosed in double quotes, and ends with `>` or `/>` for self-closing tags. The function should return `True` if the tag is well-formed, and `False` otherwise.
"""

import re

def validateHTMLTag(tag):
    pattern = r"<([a-zA-Z0-9\-_\.]+)(\s+[a-zA-Z0-9\-_\.]+\s*=\s*\"[^\"]*\")*\s*/?>"
    return bool(re.match(pattern, tag))