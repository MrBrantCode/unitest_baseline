"""
QUESTION:
Write a function `filter_words(sequence, num)` that takes a sequence of characters and a number as input. The function should return a list of words from the sequence where each word has a length greater than the input number. The function should remove all special characters from the sequence, maintaining spaces and case sensitivity, before filtering the words.
"""

import re

def filter_words(sequence, num):
    # Removing all special characters but keeping spaces
    cleaned_sequence = re.sub(r'[^\w\s]','',sequence)
    
    # Convert sequence to list of words
    words_list = cleaned_sequence.split()
    
    # Filter words by length
    filtered_words = [word for word in words_list if len(word) > num]
    
    return filtered_words