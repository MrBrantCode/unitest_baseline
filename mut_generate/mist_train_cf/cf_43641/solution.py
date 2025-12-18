"""
QUESTION:
Write a function named `clean_sentence` that takes a string as input, converts it into lowercase, and replaces any non-alphanumeric characters (except for spaces) with a space.
"""

import re

def clean_sentence(sentence):
    """
    This function takes a string as input, converts it into lowercase, 
    and replaces any non-alphanumeric characters (except for spaces) with a space.
    
    Args:
        sentence (str): The input string
    
    Returns:
        str: The cleaned sentence
    """
    # Convert the sentence into lowercase
    lowercase_sentence = sentence.lower()
    
    # Remove any aberrant symbols
    clean_sentence = re.sub(r'\W', ' ', lowercase_sentence)
    
    return clean_sentence