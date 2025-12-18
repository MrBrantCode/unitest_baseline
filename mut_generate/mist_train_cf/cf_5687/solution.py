"""
QUESTION:
Create a function called `count_occurrences` that takes two parameters: a sentence and a list of words. This function should return a dictionary where the keys are the words from the list and the values are the number of occurrences of each word in the sentence. The function should handle variations in capitalization and punctuation, as well as special characters, emojis, and non-English characters. It should be optimized for efficiency to handle large sentences and a large number of words.
"""

import re
from collections import Counter

def count_occurrences(sentence, words):
    # Remove special characters and emojis
    sentence = re.sub('[^\w\s]', '', sentence)
    # Convert sentence to lowercase
    sentence = sentence.lower()
    
    # Split the sentence into words
    sentence_words = sentence.split()
    
    # Count the occurrences of each word
    word_counts = Counter(sentence_words)
    
    # Prepare the results dictionary
    results = {word.lower(): word_counts.get(word.lower(), 0) for word in words}
    
    return results