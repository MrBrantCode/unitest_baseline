"""
QUESTION:
Write a function named `count_repeated_words` that takes a sentence as input and returns a dictionary-like object containing the count of each word that appears more than once, excluding words that contain the letter 'e' or are plural nouns (i.e., end with 's' or 'es'). The function should consider the case where a word appears multiple times in the sentence, and its output should only include words that appear more than once.
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
    
    # Filter out words that appear only once
    repeated_words = {word: count for word, count in word_counts.items() if count > 1}
    
    return repeated_words