"""
QUESTION:
Create a function `word_occurrences` that takes a string of text as input. The function should exclude non-alphabetic characters, split the text into words, and count the occurrences of each word in a case-insensitive manner. The function should return a dictionary with words that have more than six letters as keys and their respective counts as values.
"""

import re
from collections import Counter

def word_occurrences(text):
    # Remove non-alphabetic characters
    cleaned_text = re.sub('[^a-zA-Z\s]', '', text)
    
    # Convert to lowercase and split into words
    words = cleaned_text.lower().split()
    
    # Count occurrences of each word
    occurrences = Counter(words)
    
    # Create a dictionary with words that have more than six letters
    dict_word_occurrences = {word: count for word, count in occurrences.items() if len(word) > 6}
    
    return dict_word_occurrences