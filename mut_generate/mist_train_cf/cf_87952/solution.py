"""
QUESTION:
Write a function `find_phrase_frequency(text, phrase)` that finds the frequency of a given phrase in the text, considering case sensitivity, punctuation marks, and the position of the phrase in the text. The function should not count the phrase if it appears as a substring within another word.
"""

import re

def find_phrase_frequency(text, phrase):
    # Convert both text and phrase to lowercase and remove punctuation
    text = re.sub(r'[^\w\s]', '', text.lower())
    phrase = re.sub(r'[^\w\s]', '', phrase.lower())
    
    # Split text into words
    words = text.split()
    
    # Initialize counter
    frequency = 0
    
    # Iterate over words
    for word in words:
        # Check if phrase is a substring of word
        if phrase in word:
            # Check if the phrase appears as a separate word
            if re.search(r'\b{}\b'.format(phrase), word):
                frequency += 1
    
    return frequency