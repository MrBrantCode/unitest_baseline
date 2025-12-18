"""
QUESTION:
Write a function named `most_common_word` that takes a list of strings as input, where each string may contain multiple occurrences of the same word separated by different punctuation marks, and returns the word that recurs the most frequently considering both upper case and lower case occurrences. The function should be case-insensitive.
"""

import re
from collections import Counter

def most_common_word(lst):
    """
    This function takes a list of strings as input and returns the word that recurs the most frequently 
    considering both upper case and lower case occurrences. The function is case-insensitive.

    Parameters:
    lst (list): A list of strings

    Returns:
    str: The most common word
    """
    # Split the words in a string
    words = [re.findall(r'\b\w+\b', string) for string in lst]
    
    # Flatten the list of words
    words = [word.lower() for sublist in words for word in sublist]
    
    # Count the occurrences of each word
    counter = Counter(words)
    
    # Get the most common word
    return max(counter, key=counter.get)