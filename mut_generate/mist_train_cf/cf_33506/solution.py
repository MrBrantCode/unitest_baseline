"""
QUESTION:
Write a function `extract_info(code)` that takes a string `code` as input, representing a valid Python code snippet containing a comment block with creation date and author information. The creation date is in the format "Month-Day-Year Hour:Minute:Second" and the author is specified after the `@` symbol. Return a tuple `(creation_date, author)`.
"""

import re

def extract_info(code):
    comment_block = re.findall(r"'''.*?'''", code, re.DOTALL)[0]
    creation_date = re.search(r'Created on (.+?)\n', comment_block).group(1)
    author = re.search(r'@(.+?)\n', comment_block).group(1)
    return (creation_date, author)