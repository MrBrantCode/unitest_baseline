"""
QUESTION:
Extract all single-line and multi-line comments from a list of code lines, preserving their order. Single-line comments start with "//" and multi-line comments are enclosed in "/* */". Write a function `extract_comments(code: List[str]) -> List[str]` that takes a list of code lines as input and returns a list of extracted comments.
"""

from typing import List

def extract_comments(code: List[str]) -> List[str]:
    comments = []
    in_multiline_comment = False

    for line in code:
        line = line.strip()
        if line.startswith("//"):
            comments.append(line)
        elif line.startswith("/*"):
            in_multiline_comment = True
            comments.append(line)
        elif line.endswith("*/"):
            in_multiline_comment = False
            comments.append(line)
        elif in_multiline_comment:
            comments.append(line)

    return comments