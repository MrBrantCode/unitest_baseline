"""
QUESTION:
Write a function `count_unique_words(sentence)` that takes a string `sentence` as input and returns the total number of unique words, excluding repeated words and words comprised of only digits. The function should ignore case and punctuation marks.
"""

import string

def count_unique_words(sentence):
    # Remove punctuation marks
    sentence = sentence.translate(str.maketrans('', '', string.punctuation))
    
    # Split sentence into words
    words = sentence.split()
    
    # Set to store unique words
    unique_words = set()
    
    # Iterate through each word
    for word in words:
        # Skip words comprised of only digits
        if word.isdigit():
            continue
        # Add word to set of unique words
        unique_words.add(word.lower())
    
    # Return the count of unique words
    return len(unique_words)