"""
QUESTION:
Write a function `count_string_occurrences` that returns the number of occurrences of a specific string in a given text, ignoring case sensitivity and considering the string as part of other words. The function should also handle special characters and punctuation marks.
"""

import re

def count_string_occurrences(text, string):
    """
    Returns the number of occurrences of a specific string in a given text, 
    ignoring case sensitivity and considering the string as part of other words.
    
    Args:
        text (str): The text to search in.
        string (str): The string to search for.
    
    Returns:
        int: The number of occurrences of the string in the text.
    """
    # Convert both the text and the string to lower case to ignore case sensitivity
    text = text.lower()
    string = string.lower()
    
    # Use regular expression to find all occurrences of the string in the text
    occurrences = re.findall(string, text)
    
    # Return the number of occurrences
    return len(occurrences)