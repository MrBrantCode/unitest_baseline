"""
QUESTION:
Write a function called `reverse_sentence` that takes a sentence as input and returns the reversed version of that sentence, ignoring punctuation marks, special characters, and numbers. The function should handle cases where multiple spaces, tabs, or new lines are present between words and should be able to handle sentences with up to 1 million characters.
"""

import re

def reverse_sentence(sentence):
    # Remove punctuation marks, special characters, and numbers
    sentence = re.sub('[^a-zA-Z ]', '', sentence)
    
    # Split sentence into words
    words = sentence.split()
    
    # Reverse the order of words
    reversed_words = words[::-1]
    
    # Join the reversed words into a sentence
    reversed_sentence = ' '.join(reversed_words)
    
    return reversed_sentence