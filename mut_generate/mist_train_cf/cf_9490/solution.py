"""
QUESTION:
Create a function named `create_word_frequency` that takes a string sentence as input and returns a dictionary containing words and their frequencies. The function should remove any punctuation marks, convert all words to lowercase, exclude the words "the", "is", and "and", and sort the dictionary in descending order based on the word frequencies. The input string can contain any number of words and punctuation marks.
"""

import string
from collections import Counter

def create_word_frequency(sentence):
    # Remove punctuation marks
    sentence = sentence.translate(str.maketrans('', '', string.punctuation))
    
    # Convert sentence to lowercase
    sentence = sentence.lower()
    
    # Exclude common English words
    common_words = ['the', 'is', 'and']
    words = sentence.split()
    words = [word for word in words if word not in common_words]
    
    # Count word frequencies
    word_frequencies = Counter(words)
    
    # Sort dictionary in descending order based on frequencies
    sorted_word_frequencies = dict(sorted(word_frequencies.items(), key=lambda x: x[1], reverse=True))
    
    return sorted_word_frequencies