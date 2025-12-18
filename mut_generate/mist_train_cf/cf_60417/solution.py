"""
QUESTION:
Create a function `match_sequence` that takes a string `seq` as input and returns `True` if the sequence starts with two alphanumeric characters, ends with "oo", and does not contain any whitespace characters. The function should be efficient in terms of time complexity, ideally O(n), where n is the length of the string.
"""

import re

def match_sequence(seq: str) -> bool:
    pattern = r"^[a-zA-Z0-9]{2}.*oo$"
    has_no_spaces = not bool(re.search(r"\s", seq))
    return bool(re.match(pattern, seq)) and has_no_spaces