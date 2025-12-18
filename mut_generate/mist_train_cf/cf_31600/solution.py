"""
QUESTION:
Create a function `extract_metadata(code_snippet)` that takes a string `code_snippet` as input, extracts the author's name, email, and date, and returns them in a dictionary. The code snippet is expected to be in the format `__author__ = '<NAME>'`, `__email__ = '<EMAIL>'`, and `__date__ = '<DATE>'`. The function should return `None` if the input code snippet does not contain all three metadata.
"""

import re

def extract_metadata(code_snippet: str) -> dict or None:
    author_match = re.search(r'__author__ = \'(.*?)\'', code_snippet)
    email_match = re.search(r'__email__ = \'(.*?)\'', code_snippet)
    date_match = re.search(r'__date__ = \'(.*?)\'', code_snippet)

    if author_match and email_match and date_match:
        return {
            'author': author_match.group(1),
            'email': email_match.group(1),
            'date': date_match.group(1)
        }
    else:
        return None