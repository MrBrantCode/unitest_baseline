"""
QUESTION:
Develop a function called `remove_chars` that takes two parameters: `text` (the input text from which characters need to be removed) and `patterns` (a list of patterns or characters to be removed). The function should remove every occurrence of the specified patterns from the input text while preserving the original format, including spaces and punctuation. The function should handle edge cases such as null or empty text, manage multiple languages and specific characters from different languages, handle nested removals, and correctly process Unicode characters and escape sequences. Additionally, the function should be able to handle regular expressions as input for the characters to be removed and apply them in the order they are given. The function should not remove already removed characters again and only remove characters that are in the list of characters to be removed if a regular expression matches a sequence of characters that includes characters that are not in the list.
"""

import re

def remove_chars(text, patterns): 
    """
    Function to remove specified characters from text

    Parameters: 
    text (str): Input text
    patterns (list): a list of patterns (string or regex) to remove

    Returns: 
    str: Text with patterns removed
    """   

    if not text:  # handling null and empty text case
        return ""

    for pattern in patterns:
        text = re.sub(pattern, '', text)

    return text