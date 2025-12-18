"""
QUESTION:
Create a function `extract_comments(text: str) -> List[str]` that extracts all comments enclosed within triple double quotes (`""" ... """`) from the given text. The function should return a list of strings where each string represents a comment found in the input text. The input text may contain multiple comments, and its length is restricted to 1 <= len(text) <= 10^5.
"""

from typing import List

def extract_comments(text: str) -> List[str]:
    comments = []
    start = 0
    while True:
        start = text.find('"""', start)
        if start == -1:
            break
        end = text.find('"""', start + 3)
        if end == -1:
            break
        comments.append(text[start + 3:end].strip())
        start = end + 3
    return comments