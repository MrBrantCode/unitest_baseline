"""
QUESTION:
Implement a function `extract_comments` that takes a string `code` as input and returns a list of comments found in the code. Comments are denoted by the `///` prefix at the start of a line. The function should extract and return the content of these comments, excluding the prefix and any trailing newlines.
"""

import re

def extract_comments(code):
    comments = re.findall(r'///\s*(.*?)\n', code, re.DOTALL)
    return comments