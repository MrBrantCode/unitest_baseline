"""
QUESTION:
Create a function named `count_words` that takes a string `text` as input and returns a dictionary where keys are words from the text (excluding common English words "a", "the", "and") and values are their respective frequencies in the text. The function should ignore case and consider "word" and "Word" as the same word.
"""

import re

def count_words(text):
    # Define a list of common English words to exclude
    common_words = ["a", "the", "and"]
    
    # Convert the text to lowercase and split it into words
    words = re.findall(r'\w+', text.lower())
    
    # Create an empty dictionary to store the word frequencies
    word_freq = {}
    
    # Iterate over each word in the list
    for word in words:
        # Exclude common English words
        if word not in common_words:
            # Update the frequency of the word in the dictionary
            word_freq[word] = word_freq.get(word, 0) + 1
    
    return word_freq