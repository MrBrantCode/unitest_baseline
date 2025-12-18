"""
QUESTION:
Create a function called `tokenize_sentence` that takes a string as input. The function should remove punctuation marks from the string and then split it into words, but only include words that start with a capital letter.
"""

import re

def tokenize_sentence(sentence):
    """
    Tokenize the given sentence by removing punctuation marks and 
    splitting it into words that start with a capital letter.
    
    Parameters:
    sentence (str): The input sentence to be tokenized.
    
    Returns:
    list: A list of words that start with a capital letter.
    """
    # Remove punctuation marks
    sentence = re.sub(r'[^\w\s]', '', sentence)
    
    # Tokenize the sentence
    tokens = re.findall(r'\b[A-Z]\w+', sentence)
    
    return tokens