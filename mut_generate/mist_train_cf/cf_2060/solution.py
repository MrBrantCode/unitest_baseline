"""
QUESTION:
Write a function `count_words` that takes a sentence as input and returns the number of words in the sentence. A word is defined as a sequence of alphabetic characters (A-Z, a-z) that may contain hyphens (-) or apostrophes ('), but cannot start or end with a hyphen or apostrophe. The sentence may contain punctuation marks (., !, ?) and HTML tags, which should not be considered as part of a word. The word count is case-sensitive and should not include duplicate words.
"""

import re

def count_words(sentence):
    # Remove HTML tags and attributes
    sentence = re.sub("<[^>]*>", "", sentence)
    
    # Replace punctuation marks with spaces
    sentence = re.sub("[.,!?]", " ", sentence)
    
    # Split sentence into a list of words
    words = sentence.split()
    
    # Initialize word count
    word_count = 0
    
    # Define regex pattern for valid words
    word_pattern = re.compile("^[a-zA-Z]+[-']?[a-zA-Z]+$")
    
    # Check each word for validity and count valid words
    for word in words:
        if word_pattern.match(word):
            word_count += 1
    
    return word_count