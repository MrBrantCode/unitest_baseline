"""
QUESTION:
Create a function called `count_love_occurrences` that takes a string `text` as input. The function should count the occurrences of the word "love" and its variations, including capitalized ("Love"), singular possessive ("love's"), and compound words ("lovelorn", "lovely"), while ignoring HTML tags.
"""

import re

def count_love_occurrences(text):
    """
    Counts the occurrences of the word "love" and its variations, 
    ignoring HTML tags in the input string.

    Args:
    text (str): The input string to search for "love" occurrences.

    Returns:
    int: The count of "love" and its variations in the input string.
    """
    clean_text = re.sub("<.*?>", "", text)
    count = len(re.findall(r'\blove\b|\bLove\b|love\'s\b|Love\'s\b|lovel\w*', clean_text))
    return count