"""
QUESTION:
Write a function called `count_words` to count the number of words in a given sentence. A word is a sequence of alphabetic characters (A-Z, a-z) that may contain hyphens (-) or apostrophes ('), but cannot start or end with a hyphen or apostrophe. The function should exclude punctuation marks (., !, ?,), numeric characters (0-9), and consider the count case-sensitive, with no duplicate words considered.
"""

import re

def count_words(sentence):
    """
    Count the number of words in a given sentence.

    A word is a sequence of alphabetic characters (A-Z, a-z) that may contain 
    hyphens (-) or apostrophes ('), but cannot start or end with a hyphen or 
    apostrophe. The function excludes punctuation marks (., !, ?,), numeric 
    characters (0-9), and considers the count case-sensitive, with no duplicate 
    words considered.

    Args:
        sentence (str): The input sentence.

    Returns:
        int: The number of distinct words in the sentence.
    """
    words = re.findall(r"[a-zA-Z][a-zA-Z'-]*[a-zA-Z]", sentence)
    return len(set(words))