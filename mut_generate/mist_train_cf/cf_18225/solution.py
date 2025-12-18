"""
QUESTION:
Write a function `find_phrase_frequency(text, phrase)` that finds the frequency of a given phrase in the text. The function should consider case sensitivity, punctuation marks, and the position of the phrase in the text. If the phrase appears as a substring within another word, it should not be counted. The function should return the frequency of the phrase in the text.
"""

import re

def find_phrase_frequency(text, phrase):
    # Split the text into words and remove punctuation marks
    words = re.findall(r'\b\w+\b', text)
    
    # Initialize a counter for the frequency
    frequency = 0
    
    # Iterate over each word in the text
    for word in words:
        # Check if the phrase is a whole word and not a substring within another word
        if word.lower() == phrase.lower():
            # Increase the frequency if the word is the desired phrase
            frequency += 1
    
    return frequency