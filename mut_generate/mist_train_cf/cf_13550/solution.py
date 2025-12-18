"""
QUESTION:
Create a function called `word_frequency` that takes a string of text as input and returns a dictionary containing the frequency of each word in the text. The function should be case-insensitive and ignore special characters and punctuation marks. The output dictionary should have words in lowercase as keys and their corresponding frequencies as values.
"""

import re
from collections import Counter

def word_frequency(text):
    """
    This function takes a string of text as input and returns a dictionary containing 
    the frequency of each word in the text. The function is case-insensitive and 
    ignores special characters and punctuation marks.

    Parameters:
    text (str): The input string of text.

    Returns:
    dict: A dictionary with words in lowercase as keys and their corresponding 
          frequencies as values.
    """
    # Convert the text to lowercase
    text = text.lower()
    
    # Remove special characters and punctuation marks
    text = re.sub(r'[^\w\s]', '', text)
    
    # Split the text into words
    words = text.split()
    
    # Count the frequency of each word
    frequency = Counter(words)
    
    return dict(frequency)