"""
QUESTION:
Create a function called `word_frequency` that takes a string as input and returns a dictionary where the keys are the unique words in the string (case-insensitive) and the values are their corresponding frequencies. The function should exclude punctuation marks from the word count.
"""

import re
from collections import Counter

def word_frequency(s):
    """
    This function calculates the frequency of each word in a given string.
    
    Parameters:
    s (str): The input string.
    
    Returns:
    dict: A dictionary where the keys are the unique words in the string (case-insensitive) and the values are their corresponding frequencies.
    """
    
    # Convert the string to lower case
    s = s.lower()
    
    # Replace non-alphanumeric characters with spaces
    s = re.sub(r'[^a-z0-9\s]', ' ', s)
    
    # Split the string into words
    words = s.split()
    
    # Count the frequency of each word
    frequency = Counter(words)
    
    return dict(frequency)