"""
QUESTION:
Create a function called `replace_segment` that replaces a specific segment within a text string using Python's `re` module for regular expressions. The function should take three parameters: `text`, `pattern`, and `replacement`, where `text` is the string from which the pattern will be searched and replaced, `pattern` is the regular expression to match the segment, and `replacement` is the string to replace matched segments with. The function should return the modified string.
"""

import re

def replace_segment(text, pattern, replacement):
    """
    Replaces a specific segment within a text string using regular expressions.

    Args:
        text (str): The string from which the pattern will be searched and replaced.
        pattern (str): The regular expression to match the segment.
        replacement (str): The string to replace matched segments with.

    Returns:
        str: The modified string.
    """
    return re.sub(pattern, replacement, text)