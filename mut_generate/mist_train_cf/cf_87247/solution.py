"""
QUESTION:
Create a function `text_to_word_list(text)` that takes a string `text` as input, converts it into a list of words, separates the words by whitespace, ignores any punctuation marks except hyphen and apostrophe, and removes common stop words. The function should return a list of words, including numbers and words separated by hyphen or apostrophe, in lowercase. The common stop words to be removed are "the", "and", "a", "an", "in", "on", "is", "are", "was", "were", "to", "of", "for", "with", and "at".
"""

import re

def text_to_word_list(text):
    # Remove punctuation marks except hyphen and apostrophe
    text = re.sub(r'[^\w\s\'-]', '', text)
    # Convert text to lowercase
    text = text.lower()
    # Split text into words
    words = text.split()
    # Define common stop words
    stop_words = ['the', 'and', 'a', 'an', 'in', 'on', 'is', 'are', 'was', 'were', 'to', 'of', 'for', 'with', 'at']
    # Remove stop words from the word list
    words = [word for word in words if word not in stop_words]
    
    return words