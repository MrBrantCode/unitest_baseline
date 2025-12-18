"""
QUESTION:
Write a function `extract_author_and_date(code: str) -> Tuple[str, str]` that takes a string `code` representing a Python code snippet and returns a tuple containing the author's name and the creation date. The author's name is the value after the "Copyright (C)" line, and the creation date is the value after the "Created:" line. Assume the "Created:" line is always present and in the format "Created: <date and time>", and the "Copyright (C)" line is always present and in the format "Copyright (C) <year> <author>", where the author's name does not contain any digits or special characters.
"""

from typing import Tuple

def extract_author_and_date(code: str) -> Tuple[str, str]:
    lines = code.split('\n')
    author = None
    created = None

    for line in lines:
        if line.startswith("# Created:"):
            created = line.split("# Created:")[1].strip()
        elif line.startswith("# Copyright (C)"):
            author = line.split("Copyright (C)")[1].split()[1]

    return author, created