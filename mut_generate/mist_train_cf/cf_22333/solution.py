"""
QUESTION:
Create a function `count_words(sentence)` that takes a sentence as input, removes numbers and punctuation, and counts the frequency of each word excluding common words "the", "is", and "to". The function should be case-insensitive and return the words and their frequencies in descending order based on their frequency.
"""

import re
from collections import Counter

def count_words(sentence):
    """
    Removes numbers and punctuation from a sentence, counts the frequency of each word 
    excluding common words "the", "is", and "to", and returns the words and their frequencies 
    in descending order based on their frequency.

    Parameters:
    sentence (str): The input sentence.

    Returns:
    list: A list of tuples containing the words and their frequencies.
    """

    # Remove numbers from the sentence
    sentence = re.sub(r'\d+', '', sentence)
    
    # Remove punctuation and convert the sentence to lowercase
    sentence = re.sub(r'[^\w\s]', '', sentence.lower())
    
    # Define the list of common words to be excluded
    common_words = ['the', 'is', 'to']
    
    # Split the sentence into words
    words = sentence.split()
    
    # Count the frequency of each word, excluding common words
    word_counts = Counter(word for word in words if word not in common_words)
    
    # Sort the words and their frequencies in descending order
    sorted_word_counts = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)
    
    return sorted_word_counts