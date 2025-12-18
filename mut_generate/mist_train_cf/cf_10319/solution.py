"""
QUESTION:
Create a function named count_words that takes a sentence as input and returns the number of words in the sentence. A word is defined as a sequence of alphabetic characters (A-Z, a-z) that may contain hyphens (-) or apostrophes (') but cannot start or end with a hyphen or apostrophe. The function should ignore punctuation marks (., !, ?, etc.) and numeric characters (0-9) when counting words.
"""

import re

def count_words(sentence):
    """
    This function takes a sentence as input and returns the number of words in the sentence.
    
    A word is defined as a sequence of alphabetic characters (A-Z, a-z) that may contain 
    hyphens (-) or apostrophes (') but cannot start or end with a hyphen or apostrophe.
    
    The function ignores punctuation marks (., !, ?, etc.) and numeric characters (0-9) 
    when counting words.
    """
    
    # Remove punctuation and numeric characters from the sentence
    cleaned_sentence = re.sub(r'[^\w\s\-\']', '', sentence)
    
    # Split the sentence into words
    words = cleaned_sentence.split()
    
    # Return the number of words in the sentence
    return len(words)