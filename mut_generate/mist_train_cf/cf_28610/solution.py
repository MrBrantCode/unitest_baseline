"""
QUESTION:
Create a function `count_word_occurrences` that takes two parameters: a string `text` and a list of words `words`. The function should count the occurrences of each word in the text in a case-insensitive manner, ignoring punctuation marks. The function should return a dictionary with the words as keys and their corresponding counts as values. The counts should be in the same order as the words appear in the `words` list.
"""

import re

def count_word_occurrences(text, words):
    word_counts = {word.lower(): 0 for word in words}
    text = re.sub(r'[^\w\s]', '', text).lower()  # Remove punctuation and convert to lower case
    words_in_text = text.split()
    
    for word in words_in_text:
        if word in word_counts:
            word_counts[word] += 1
    
    # sort the word_counts by the original order of words
    sorted_word_counts = {word: word_counts[word] for word in [word.lower() for word in words]}
    
    return sorted_word_counts