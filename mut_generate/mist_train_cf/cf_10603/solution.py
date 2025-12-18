"""
QUESTION:
Write a function `count_words(text)` that takes a string `text` as input and returns the total number of words in the text, excluding any punctuation marks or special characters. The function should be able to handle large text inputs with multiple paragraphs.
"""

import string

def count_words(text):
    # Remove punctuation marks and special characters
    text = text.translate(str.maketrans('', '', string.punctuation))
    
    # Split the text into words
    words = text.split()
    
    # Count the number of words
    word_count = len(words)
    
    return word_count