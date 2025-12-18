"""
QUESTION:
Write a function `remove_tag(s, tag)` that takes a string `s` and a tag name `tag` as input, and returns a string where all occurrences of the specified tag and its corresponding value are removed. The tags are enclosed in curly brackets `{}` and the values are followed by a semicolon `;`. The tag and its value should be removed completely, including the semicolon.
"""

import re

def remove_tag(s, tag):
    p = '{' + tag + '}' + '[^;]*;'
    return re.sub(p, '', s)