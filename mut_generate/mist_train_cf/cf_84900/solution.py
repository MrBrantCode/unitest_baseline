"""
QUESTION:
Write a function named `join_text_segments` to concatenate a list of text segments into a single string with a specified delimiter. The function should take two parameters: `delimiter` and `text_segments`. The `delimiter` is the string used to separate the text segments, and `text_segments` is a list of strings. Return the concatenated string.
"""

def join_text_segments(delimiter, text_segments):
    """
    Concatenates a list of text segments into a single string with a specified delimiter.

    Args:
        delimiter (str): The string used to separate the text segments.
        text_segments (list): A list of strings to be concatenated.

    Returns:
        str: The concatenated string.
    """
    return delimiter.join(text_segments)