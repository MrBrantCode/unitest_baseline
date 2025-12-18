"""
QUESTION:
Create a function `wrap_title` that takes a string `title` and an integer `ideal_chars_per_line` as input and returns a string that is a wrapped version of `title` with a maximum of `ideal_chars_per_line` characters per line. The function should not lose any information from the original string. Use this function to set a multi-line title for a matplotlib plot.
"""

import textwrap

def wrap_title(title, ideal_chars_per_line):
    """
    Returns a string that is a wrapped version of 'title' with a maximum of 'ideal_chars_per_line' characters per line.

    Parameters:
    title (str): The title to be wrapped.
    ideal_chars_per_line (int): The maximum number of characters per line.

    Returns:
    str: The wrapped title.
    """
    return textwrap.fill(title, ideal_chars_per_line)