"""
QUESTION:
Extract Unique Words from Sentence
Write a Python function named `extract_unique_words` that takes a string `sentence` as input and returns a list of unique words. The function should remove any punctuation, convert words to lowercase, and store unique words in a list while handling sentences with multiple lines and special characters. The function should also remove leading or trailing whitespace from each word and handle different cases.
"""

import re

def extract_unique_words(sentence):
    """
    Extracts unique words from a sentence.

    Args:
        sentence (str): The input sentence.

    Returns:
        list: A list of unique words.
    """
    # Remove punctuation and special characters
    clean_sentence = re.sub(r'[^\w\s]', '', sentence)
    
    # Convert to lowercase and split into words
    words = clean_sentence.lower().split()
    
    # Remove leading and trailing whitespace from each word
    words = [word.strip() for word in words]
    
    # Store unique words in a list
    unique_words = list(set(words))
    
    return unique_words