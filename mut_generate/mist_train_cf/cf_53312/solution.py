"""
QUESTION:
Write a function named `word_frequency` that takes a sentence as input, removes punctuation, converts all words to lower case, and returns a dictionary where each unique word is a key and its corresponding frequency count in the sentence is the associated value.
"""

import re

def word_frequency(sentence):
    """
    This function takes a sentence as input, removes punctuation, 
    converts all words to lower case, and returns a dictionary 
    where each unique word is a key and its corresponding frequency 
    count in the sentence is the associated value.

    Args:
    sentence (str): The input sentence.

    Returns:
    dict: A dictionary where each unique word is a key and its 
    corresponding frequency count in the sentence is the associated value.
    """
    
    # Normalize words, remove punctuation (keep only alphanumeric and spaces), and convert to lower case
    words = re.sub(r'\W',' ', sentence).lower().split()
    
    # Build dictionary
    dict_count = {w: words.count(w) for w in words}
    
    return dict_count