"""
QUESTION:
Write a function named `count_words` that takes a string as input and returns a dictionary where the keys are unique words from the string and the values are their respective counts. The function should ignore case, non-alphabetic characters, and consider only alphabetic words.
"""

import re
from collections import Counter

def count_words(text):
    """
    This function takes a string as input, ignores case and non-alphabetic characters,
    and returns a dictionary where the keys are unique words from the string and 
    the values are their respective counts.

    Parameters:
    text (str): The input string to be analyzed.

    Returns:
    dict: A dictionary containing the unique words and their counts.
    """
    # Convert the text to lowercase and remove any non-alphabetic characters
    words = re.findall(r'\b\w+\b', text.lower())
    
    # Count the occurrence of each unique word
    return dict(Counter(words))