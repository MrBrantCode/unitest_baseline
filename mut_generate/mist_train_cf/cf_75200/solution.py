"""
QUESTION:
Create a function named word_freq that takes in one or more sentences as input and returns a dictionary where the keys are the distinct words and the values are their respective frequencies. The function should ignore punctuation marks and case sensitivity, handle contractions as single words, and correctly handle sentences with missing spaces after punctuation.
"""

import re
from collections import Counter

def word_freq(sentence):
    """
    This function takes in one or more sentences as input and returns a dictionary 
    where the keys are the distinct words and the values are their respective frequencies.
    
    Parameters:
    sentence (str): One or more sentences.
    
    Returns:
    dict: A dictionary with words as keys and their frequencies as values.
    """
    
    # Convert the sentence to lower case to ignore case sensitivity
    sentence = sentence.lower()
    
    # Use regular expression to replace non-alphanumeric characters with spaces
    sentence = re.sub(r'[^a-z0-9\s]', ' ', sentence)
    
    # Split the sentence into words
    words = sentence.split()
    
    # Count the frequency of each word
    freq = Counter(words)
    
    return dict(freq)