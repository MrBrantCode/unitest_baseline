"""
QUESTION:
Write a function `extractAuthorInfo` that takes a string representing a comment block as input. The function should extract the author's name and email from the comment block, where the author's name and email are enclosed within double angle brackets (<< >>). Return a dictionary with the keys "name" and "email" containing the extracted author's name and email. If the author's name or email is not found, the corresponding value in the dictionary should be an empty string.
"""

import re

def extractAuthorInfo(comment_block):
    author_info = {"name": "", "email": ""}

    match = re.search(r"<<(.*?)>>(.*?)>>", comment_block)
    if match:
        author_info["name"] = match.group(1).strip()
        author_info["email"] = match.group(2).strip()

    return author_info