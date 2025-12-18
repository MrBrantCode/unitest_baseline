"""
QUESTION:
Create a function named "word_frequency" that takes two parameters: a sentence and a list of stop words. The function should convert the sentence to lowercase, split it into individual words, remove any words that are in the stop words list (case-insensitive), and return a dictionary where the keys are the remaining words and the values are their frequencies. The function should be able to handle any input sentence and list of stop words.
"""

from collections import Counter

def word_frequency(sentence, stop_words):
    # Convert to lowercase and split into words
    words = sentence.lower().split()
    
    # Remove stop words
    words = [word for word in words if word.lower() not in [stop_word.lower() for stop_word in stop_words]]
    
    # Calculate frequency of each word
    word_freq = dict(Counter(words))
    
    return word_freq