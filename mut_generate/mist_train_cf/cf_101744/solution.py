"""
QUESTION:
Extract adjectives describing uncommon colors from a text file in Python. 

Create a function named `extract_less_common_colors` to filter out the commonly used colors from a given text and return only the less common ones. Assume that common colors are predefined as ["red", "orange", "yellow", "green", "blue", "purple", "pink", "brown", "black", "white", "gray", "grey"]. The function should use regular expressions to match adjectives that describe colors in the text.
"""

import re

def extract_less_common_colors(text, common_colors):
    """
    Extract adjectives describing uncommon colors from a text.

    Args:
    text (str): The input text to extract colors from.
    common_colors (list): A list of common colors.

    Returns:
    list: A list of less common color adjectives.
    """
    # Regular expression to match adjectives that describe colors
    color_regex = re.compile(r'\b([A-Z][a-z]*s? ?[A-Z][a-z]*s? ?[A-Z][a-z]*s? ?[A-Z][a-z]*)\b')
    # Find all matches of the color regex in the text
    matches = color_regex.findall(text)
    # Filter out the common colors
    less_common_colors = [match.lower() for match in matches if match.lower() not in common_colors]
    return less_common_colors