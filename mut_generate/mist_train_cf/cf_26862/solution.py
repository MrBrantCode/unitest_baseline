"""
QUESTION:
Implement a function named `commentizer` that takes a boolean value `answer2` and a list of comments as input, and returns a tuple containing the updated list of comments and a boolean value `is_correct`. If `answer2` is True, set `is_correct` to True and return the original list of comments. If `answer2` is False, set `is_correct` to False and append "Open the site and try changing `cover` to `contain` in DevTools to see the difference." and "Check the first one." to the list of comments.
"""

from typing import List, Tuple

def commentizer(answer2: bool, comments: List[str]) -> Tuple[List[str], bool]:
    is_correct = answer2
    if not answer2:
        is_correct = False
        comments.append("Open the site and try changing `cover` to `contain` in DevTools to see the difference.")
        comments.append("Check the first one.")
    return comments, is_correct