"""
QUESTION:
Create a function `parse_code_snippet(code: str) -> (str, str)` that takes a code snippet as input, extracts the GitHub stars range from the `<gh_stars>` tag and the comment associated with the pylint disable directive enclosed within triple quotes, and returns a tuple containing these two extracted values. The input code snippet will always contain the `<gh_stars>` tag and the pylint disable directive comment.
"""

import re

def entance(code: str) -> (str, str):
    stars_match = re.search(r'<gh_stars>(\d+-\d+)', code)
    comment_match = re.search(r"'''(.*?)'''", code, re.DOTALL)
    stars = stars_match.group(1) if stars_match else ''
    comment = comment_match.group(1).strip() if comment_match else ''
    return stars, comment