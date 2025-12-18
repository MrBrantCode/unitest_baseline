"""
QUESTION:
Create a function named `count_lexical_items` that takes a string of words as input and returns a dictionary containing the recurring words and their counts. The function should be case-insensitive and consider punctuation as part of the words.
"""

from collections import defaultdict

def count_lexical_items(sentence):
    word_count = defaultdict(int)
    words = sentence.split()
    
    for word in words:
        word_count[word.lower()] += 1

    recurring_words = {word: count for word, count in word_count.items() if count > 1}

    return recurring_words