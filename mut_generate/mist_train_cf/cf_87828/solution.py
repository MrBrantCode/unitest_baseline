"""
QUESTION:
Create a function called `word_frequency` that takes a string as input, converts it to all uppercase, removes any punctuation marks, counts the frequency of each word, and returns the words in descending order of their frequency. The function should not take any other arguments.
"""

import re
from collections import Counter

def word_frequency(text):
    """
    This function takes a string as input, converts it to all uppercase, 
    removes any punctuation marks, counts the frequency of each word, 
    and returns the words in descending order of their frequency.

    Args:
        text (str): The input string.

    Returns:
        list: A list of tuples containing the words and their frequencies.
    """
    # Convert to uppercase and remove punctuation marks
    text = re.sub(r'[^\w\s]', '', text.upper())
    
    # Count the frequency of each word
    word_count = Counter(text.split())
    
    # Sort the words in descending order of their frequency
    sorted_words = sorted(word_count.items(), key=lambda x: x[1], reverse=True)
    
    return sorted_words