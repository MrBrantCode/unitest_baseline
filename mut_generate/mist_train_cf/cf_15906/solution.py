"""
QUESTION:
Write a function `count_repeated_words` that takes a sentence as input, splits it into words, and returns a dictionary-like object where keys are the words and values are their frequencies, excluding any words that contain the letter 'e' and are plural nouns (i.e., words ending in 's' or 'es').
"""

from collections import Counter

def count_repeated_words(sentence):
    # Split the sentence into words
    words = sentence.split()
    
    # Exclude words containing the letter 'e' and are plural nouns
    excluded_words = set()
    for word in words:
        if 'e' in word or word.endswith('s') or word.endswith('es'):
            excluded_words.add(word)
    
    # Count the repeated words
    word_counts = Counter(word for word in words if word not in excluded_words)
    
    return word_counts