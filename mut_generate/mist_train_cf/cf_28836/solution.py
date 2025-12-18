"""
QUESTION:
Write a function `count_pattern_occurrences` that takes two parameters: `pattern` and `text`. Using the `re` module, count the number of occurrences of `pattern` in `text` and return the count. The `pattern` parameter should be treated as a literal string and not a regular expression.
"""

import re

def count_pattern_occurrences(pattern, text):
    """
    Counts the number of occurrences of a literal pattern in a given text.

    Args:
        pattern (str): The literal pattern to search for.
        text (str): The text to search for the pattern.

    Returns:
        int: The number of occurrences of the pattern in the text.
    """
    # Escape the pattern to treat it as a literal string
    escaped_pattern = re.escape(pattern)
    matches = re.findall(escaped_pattern, text)
    return len(matches)