"""
QUESTION:
Regex Failure - Bug Fixing #2
Oh no, Timmy's received some hate mail recently but he knows better. Help Timmy fix his regex filter so he can be awesome again!
"""

import re

def filter_negative_words(phrase: str) -> str:
    """
    Filters out specified negative words from the input phrase and replaces them with 'awesome'.

    Parameters:
    phrase (str): The input text to be filtered.

    Returns:
    str: The filtered text with negative words replaced by 'awesome'.
    """
    return re.sub(r'(bad|mean|ugly|horrible|hideous)', 'awesome', phrase, flags=re.IGNORECASE)