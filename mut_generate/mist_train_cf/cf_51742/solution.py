"""
QUESTION:
Write a function `find_six_letter_word` that uses a regular expression to find a six-letter word that starts with 'a' and ends with 's'. The function should return a list of all such words found in a given text. The regular expression should ensure that the word starts with 'a' and ends with 's', and that it is a whole word (i.e., not part of another word).
"""

import re

def find_six_letter_word(text):
    """
    This function uses a regular expression to find a six-letter word 
    that starts with 'a' and ends with 's' in a given text.

    Args:
        text (str): The text to search for six-letter words.

    Returns:
        list: A list of all six-letter words found in the text that start with 'a' and end with 's'.
    """
    regex = r"\ba[a-z]{4}s\b"
    return re.findall(regex, text)