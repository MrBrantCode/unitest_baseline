"""
QUESTION:
Construct a regular expression pattern to match words that start with a capital letter. The pattern should match any word that begins with an uppercase letter (A-Z) and is followed by zero or more word characters.
"""

def entrance(s):
    """
    Returns True if the string starts with a capital letter, False otherwise.
    
    :param s: The input string.
    :return: A boolean value indicating whether the string starts with a capital letter.
    """
    import re
    pattern = r'\b[A-Z]\w+'
    return bool(re.match(pattern, s))