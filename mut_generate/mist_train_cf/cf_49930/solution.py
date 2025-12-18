"""
QUESTION:
Design a function `sort_words_by_len` that takes a list of words as input and returns the list sorted by the length of the words, excluding special characters, and in case of a tie, sorts them alphabetically in a case-insensitive manner. The function should handle duplicates and return the original words with their original case.
"""

import re

def sort_words_by_len(list_of_words):
    word_lengths = []
    for word in list_of_words:
        clean_word = re.sub(r'\W+', '', word) 
        word_lengths.append((len(clean_word), word.lower(), word)) 
        
    word_lengths.sort() 
    return [word[2] for word in word_lengths]