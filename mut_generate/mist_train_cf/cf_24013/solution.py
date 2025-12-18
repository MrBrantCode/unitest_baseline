"""
QUESTION:
Create a function `censor_text` that takes a string as input and returns the string with all words containing 4 letters or more replaced with "*****".
"""

def censor_text(text):
    """
    Replaces all words containing 4 letters or more with "*****" in a given string.

    Args:
        text (str): The input string.

    Returns:
        str: The string with all words containing 4 letters or more replaced with "*****".
    """
    return ' '.join(['*****' if len(word) >= 4 else word for word in text.split()])